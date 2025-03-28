from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import User
from django.contrib.auth import authenticate


# Serializer for user registration
class RegisterSerializer(serializers.ModelSerializer):
    # Declaring a password field, ensuring it's write-only (it will not be included in serialized responses)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User  # Associating this serializer with the custom User model
        fields = ('username', 'email', 'password')  # Fields that will be serialized/deserialized

    # Overriding the create method to handle user creation
    def create(self, validated_data):
        # Create a new User instance but don't save it to the database yet
        user = User(
            username=validated_data['username'],  # Assign the validated username
            email=validated_data['email']  # Assign the validated email
        )
        # Set the password using Django's built-in password hashing mechanism
        user.set_password(validated_data['password'])
        # Save the user to the database
        user.save()
        return user  # Return the created user instance

# Serializer for user login/authentication
class LoginSerializer(serializers.Serializer):
    # Username and password fields that will be passed to the serializer during login
    username = serializers.CharField()
    password = serializers.CharField()

    # Custom validation method to authenticate the user with the provided credentials
    def validate(self, data):
        # Authenticate the user using the provided username and password
        user = authenticate(**data)
        # If authentication fails, raise a validation error with a custom message
        if user is None:
            raise serializers.ValidationError("Invalid credentials")
        return user  # If successful, return the authenticated user



# Serializer to handle password change
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)


# Serializer to handle password reset request
class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        # Check if the email exists in the system
        user_model = get_user_model()
        if not user_model.objects.filter(email=value).exists():
            raise serializers.ValidationError("User with this email does not exist.")
        return value


# Serializer to handle password reset confirmation
class PasswordResetConfirmSerializer(serializers.Serializer):
    uidb64 = serializers.CharField()
    token = serializers.CharField()
    new_password = serializers.CharField(write_only=True)

    def validate(self, data):
        # Additional validation can be added if needed
        return data