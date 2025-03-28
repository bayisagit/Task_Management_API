from rest_framework import serializers  # Import the serializers module from Django REST Framework
from .models import Category  # Import the Category model

class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.
    Used to validate and serialize category data for API responses.
    """

    class Meta:
        model = Category  # Specify the model to be serialized
        fields = ['id', 'name']  # Define the fields to be included in the serialized output