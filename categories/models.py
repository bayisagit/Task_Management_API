from django.db import models  # Import the models module from Django to define database models
from django.contrib.auth.models import User  # Import the User model for user management

class Category(models.Model):
    """
    Model representing a task category.
    Each category is associated with a specific user.
    """

    name = models.CharField(max_length=100)  # Name of the category, with a maximum length of 100 characters
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')
    # Foreign key linking to the User model; a category belongs to a user.
    # If the user is deleted, all associated categories will also be deleted (cascade).
    # 'related_name' allows accessing the categories of a user via user.categories.

    def __str__(self):
      
        return self.name  # Returns the category name as a string