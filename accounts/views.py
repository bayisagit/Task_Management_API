from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from django.contrib.auth import get_user_model, authenticate, login, logout
from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    ChangePasswordSerializer,
    PasswordResetSerializer,
    PasswordResetConfirmSerializer,
)
from rest_framework import generics

class RegisterView(generics.CreateAPIView):
    """
    View for user registration.
    Allows new users to create an account by providing a username, email, and password.
    """
    serializer_class = RegisterSerializer  # Specify the serializer to be used for validation and creation
    permission_classes = [AllowAny]  # Allow any user (authenticated or not) to access this view

class LoginView(generics.GenericAPIView):
    """
    View for user login.
    Authenticates the user and provides a token for subsequent API requests.
    """
    serializer_class = LoginSerializer  # Specify the serializer for login
    permission_classes = [AllowAny]  # Allow any user to access this view

    def post(self, request, *args, **kwargs):
        """
        Handle POST request for user login.
        Validates the provided credentials and returns an authentication token.
        """
        # Get the serializer instance with the request data
        serializer = self.get_serializer(data=request.data)

        # Validate the serializer and raise an exception if validation fails
        serializer.is_valid(raise_exception=True)

        # Retrieve the authenticated user from the validated data
        user = serializer.validated_data

        # Get or create an authentication token for the user
        token, _ = Token.objects.get_or_create(user=user)

        # Return the token in the response
        return Response({'token': token.key})

class LogoutView(generics.GenericAPIView):
    """
    View for user logout.
    Deletes the user's authentication token to log them out.
    """
    def post(self, request):
        """
        Handle POST request for user logout.
        Deletes the token associated with the authenticated user.
        """
        # Delete the user's auth token to log them out
        request.user.auth_token.delete()

        # Return a 204 No Content response to indicate successful logout
        return Response(status=status.HTTP_204_NO_CONTENT)

# View to handle password change
class ChangePasswordView(APIView):
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if not user.check_password(serializer.validated_data['old_password']):
                return Response({"detail": "Old password is incorrect"}, status=status.HTTP_400_BAD_REQUEST)
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({"detail": "Password changed successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# View to handle password reset request
class PasswordResetView(APIView):
    serializer_class = PasswordResetSerializer
    permission_classes = [AllowAny]  # Allow unauthenticated users
    
    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                # Fetch the user by email
                user = get_user_model().objects.get(email=email)
            except get_user_model().DoesNotExist:
                return Response({"detail": "User with this email does not exist."}, status=status.HTTP_400_BAD_REQUEST)

            # Generate token and UID
            uid = urlsafe_base64_encode(str(user.pk).encode())
            token = default_token_generator.make_token(user)
            
            # Construct the reset URL
            reset_url = f"{settings.FRONTEND_RESET_URL.format(uid=uid, token=token)}"
            
            # Send reset email
            subject = "Password Reset Request"
            message = f"Click the link to reset your password: {reset_url}"
            send_mail(subject, message, 'no-reply@yourdomain.com', [email])
            
            return Response({"detail": "Password reset link sent to email"}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# View to handle password reset confirmation
class PasswordResetConfirmView(APIView):
    serializer_class=PasswordResetConfirmSerializer
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = PasswordResetConfirmSerializer(data=request.data)
        if serializer.is_valid():
            try:
                # Decode the UID and validate the token
                uidb64 = serializer.validated_data['uidb64']
                token = serializer.validated_data['token']
                uid = urlsafe_base64_decode(uidb64).decode()
                user = get_user_model().objects.get(pk=uid)
                
                # Check if the token is valid
                if not default_token_generator.check_token(user, token):
                    return Response({"detail": "Invalid token or token expired."}, status=status.HTTP_400_BAD_REQUEST)
                
                # Reset the password
                user.set_password(serializer.validated_data['new_password'])
                user.save()
                return Response({"detail": "Password has been reset successfully."}, status=status.HTTP_200_OK)
            
            except (get_user_model().DoesNotExist, ValueError):
                return Response({"detail": "Invalid UID or user does not exist."}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)