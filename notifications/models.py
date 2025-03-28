from django.db import models  # Import the models module from Django to define database models
from django.contrib.auth.models import User  # Import the User model for user management
from tasks.models import Task  # Import the Task model for task-related notifications

class Notification(models.Model):
    """
    Model representing notifications for tasks.
    Each notification is associated with a specific user and may relate to a task.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    # Foreign key linking to the User model; a notification belongs to a user.
    # If the user is deleted, all associated notifications will also be deleted (cascade).
    # 'related_name' allows accessing the notifications of a user via user.notifications.

    message = models.TextField()  # Content of the notification, stored as text

    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, blank=True)
    # Foreign key linking to the Task model; a notification can be related to a specific task.
    # If the task is deleted, the notification will remain but with a null task reference.
    # 'null=True' and 'blank=True' allow the task field to be optional.

    is_read = models.BooleanField(default=False)  # Indicates whether the notification has been read by the user

    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of when the notification was created

    def __str__(self):
        """
        String representation of the Notification object.
        This method returns a readable string representation for instances of the notification.
        """
        return f"Notification for {self.user.username}: {self.message}"  # Returns a formatted string with user info and message