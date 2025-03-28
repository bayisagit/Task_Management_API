from django.db import models  # Import the models module from Django to define database models
from django.contrib.auth.models import User  # Import the User model for user management
from categories.models import Category  # Import the Category model for task categorization
from django.utils import timezone
from django.core.exceptions import ValidationError

class Task(models.Model):
    """
    Model representing a task.
    Each task is associated with a specific user and may belong to a category.
    """

    # Define choices for task priority levels
    TITLE_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    # Define choices for task status
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    # Foreign key linking to the User model; each task belongs to a specific user.
    # If the user is deleted, all associated tasks will also be deleted (cascade).
    # 'related_name' allows accessing the tasks of a user via user.tasks.

    title = models.CharField(max_length=100)  # Title of the task, with a maximum length of 100 characters
    description = models.TextField()  # Detailed description of the task
    due_date = models.DateTimeField()  # The date and time by which the task should be completed
    priority = models.CharField(max_length=10, choices=TITLE_CHOICES)  # Priority level of the task
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')  # Current status of the task
    completed_at = models.DateTimeField(null=True, blank=True)  # Timestamp of when the task was marked as completed (nullable)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')
    # Foreign key linking to the Category model; a task can belong to a specific category.
    # If the category is deleted, the task will retain its data but with a null category reference.
    # 'null=True' and 'blank=True' allow the category field to be optional.

    def clean(self):
        if self.due_date <= timezone.now():
            raise ValidationError("Due date must be in the future.")

    def save(self, *args, **kwargs):
        self.full_clean()  # Call clean() before saving
        super().save(*args, **kwargs)