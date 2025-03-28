from rest_framework import viewsets, permissions  # Import viewsets and permissions from DRF
from rest_framework.response import Response  # Import Response class to return responses
from .models import Category  # Import the Category model
from .serializers import CategorySerializer  # Import the CategorySerializer

class CategoryViewSet(viewsets.ViewSet):
    """
    ViewSet for managing categories.
    Provides functionality to list, create, retrieve, update, and delete categories.
    """
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can access these endpoints

    def list(self, request):
        """
        Retrieve a list of all categories for the authenticated user.
        """
        # Filter categories based on the authenticated user
        categories = Category.objects.filter(user=request.user)
        # Serialize the category data for response
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)  # Return serialized data in the response

    def retrieve(self, request, pk=None):
        """
        Retrieve a specific category by ID.
        """
        category = self.get_object(pk)  # Get the category object
        serializer = CategorySerializer(category)  # Serialize the category data
        return Response(serializer.data)  # Return serialized data in the response

    def create(self, request):
        """
        Create a new category for the authenticated user.
        """
        serializer = CategorySerializer(data=request.data)  # Initialize serializer with request data
        if serializer.is_valid():  # Validate the data
            serializer.save(user=request.user)  # Save the category with the authenticated user
            return Response(serializer.data, status=201)  # Return the created category data with 201 status
        return Response(serializer.errors, status=400)  # Return errors with 400 status if invalid

    def update(self, request, pk=None):
        """
        Update a specific category by ID.
        """
        category = self.get_object(pk)  # Get the category object to update
        serializer = CategorySerializer(category, data=request.data)  # Initialize serializer with request data
        if serializer.is_valid():  # Validate the updated data
            serializer.save()  # Save the updated category
            return Response(serializer.data)  # Return the updated category data
        return Response(serializer.errors, status=400)  # Return errors if invalid

    def destroy(self, request, pk=None):
        """
        Delete a specific category by ID.
        """
        category = self.get_object(pk)  # Get the category object to delete
        category.delete()  # Delete the category
        return Response(status=204)  # Return a 204 No Content response

    def get_object(self, pk):
        """
        Helper method to retrieve a category by ID.
        Returns a 404 response if the category does not exist.
        """
        try:
            return Category.objects.get(pk=pk, user=self.request.user)  # Get the category for the authenticated user
        except Category.DoesNotExist:
            return Response(status=404)  # Return 404 if the category does not exist