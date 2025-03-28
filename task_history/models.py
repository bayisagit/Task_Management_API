from django.db import models  # Import the models module from Django to define database models
from tasks.models import Task  # Import the Task model for referencing tasks in the history

class TaskHistory(models.Model):
    """
    Model representing the history of a task.
    This model tracks changes in the status of a task over time.
    """

    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='history')
    # Foreign key linking to the Task model; each history entry is associated with a specific task.
    # If the task is deleted, all associated history entries will also be deleted (cascade).
    # 'related_name' allows accessing the history entries of a task via task.history.

    status = models.CharField(max_length=10)  # Current status of the task at the time of this history entry

    changed_at = models.DateTimeField(auto_now_add=True)  # Timestamp of when the status was changed

    def __str__(self):
        """
        String representation of the TaskHistory object.
        Returns a readable string representation for instances of the task history.
        """
        return f"{self.task.title} - {self.status} on {self.changed_at}"  # Returns a formatted string with task title, status, and timestamp