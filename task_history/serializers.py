from rest_framework import serializers  # Import the serializers module from Django REST Framework
from .models import TaskHistory  # Import the TaskHistory model

class TaskHistorySerializer(serializers.ModelSerializer):
    """
    Serializer for the TaskHistory model.
    Used to validate and serialize task history data for API responses.
    """

    class Meta:
        model = TaskHistory  # Specify the model to be serialized
        fields = '__all__'  # Include all fields from the TaskHistory model in the serialized output