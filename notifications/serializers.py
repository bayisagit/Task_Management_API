from rest_framework import serializers  # Import the serializers module from Django REST Framework
from .models import Notification  # Import the Notification model

class NotificationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Notification model.
    Used to validate and serialize notification data for API responses.
    """

    class Meta:
        model = Notification  # Specify the model to be serialized
        fields = '__all__'  # Include all fields from the Notification model in the serialized output