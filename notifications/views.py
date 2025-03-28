from django.core.mail import send_mail  # Import the send_mail function to send email notifications
from rest_framework import viewsets, permissions  # Import viewsets and permissions from Django REST Framework
from .models import Notification  # Import the Notification model
from .serializers import NotificationSerializer  # Import the Notification serializer

class NotificationViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing notifications.
    Provides functionality to list, create, retrieve, update, and delete notifications for users.
    """
    serializer_class = NotificationSerializer  # Specify the serializer for the Notification model
    permission_classes = [permissions.IsAuthenticated]  # Ensure that only authenticated users can access these endpoints

    def get_queryset(self):
        """
        Retrieve the notifications for the authenticated user.
        """
        return Notification.objects.filter(user=self.request.user)  # Filter notifications by the current user

def send_task_notification(task):
    """
    Send an email notification for a task that is due soon.

    Parameters:
    task (Task): The task object for which the notification is being sent.
    """
    # Prepare and send the email notification
    send_mail(
        'Task Due Reminder',  # Subject of the email
        f'Your task "{task.title}" is due soon.',  # Body of the email
        'from@example.com',  # Sender's email address
        [task.user.email],  # Recipient's email address (user associated with the task)
        fail_silently=False,  # Raise an error if sending fails
    )