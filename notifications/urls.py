from django.urls import path  # Import the path function to define URL patterns
from .views import NotificationViewSet  # Import the NotificationViewSet to map URLs to view functions

urlpatterns = [
    # URL pattern for listing notifications
    path('', NotificationViewSet.as_view({'get': 'list'}), name='notification-list'),
    # This maps the root URL for notifications to the list method of NotificationViewSet
    # It allows authenticated users to retrieve their list of notifications
]