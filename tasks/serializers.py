from rest_framework import serializers  # Import the serializers module from Django REST Framework
from .models import Task  # Import the Task model

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the Task model.
    Used to validate and serialize task data for API responses.
    """

    class Meta:
        model = Task  # Specify the model to be serialized
        fields = '__all__'  # Include all fields from the Task model in the serialized output