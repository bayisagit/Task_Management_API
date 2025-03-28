from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    LogoutView,
    ChangePasswordView,
    PasswordResetView,
    PasswordResetConfirmView,
)

urlpatterns = [
   path('register/', RegisterView.as_view(), name='register'),  # Maps to the RegisterView for handling user registration

    # URL pattern for user login
    path('login/', LoginView.as_view(), name='login'),  # Maps to the LoginView for handling user authentication

    # URL pattern for user logout
    path('logout/', LogoutView.as_view(), name='logout'),  # Maps to the LogoutView for logging out the user
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset-confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]