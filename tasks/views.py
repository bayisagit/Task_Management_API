from rest_framework import viewsets, permissions  # Import viewsets and permissions from Django REST Framework
from rest_framework.response import Response  # Import Response class to return responses
from .models import Task  # Import the Task model
from .serializers import TaskSerializer  # Import the Task serializer
from notifications.models import Notification  # Import the Notification model for sending notifications

class TaskViewSet(viewsets.ViewSet):
    """
    ViewSet for managing tasks.
    Provides functionality to list, create, retrieve, update, and delete tasks.
    """
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can access these endpoints

    def list(self, request):
        """
        Retrieve a list of all tasks for the authenticated user.
        """
        tasks = Task.objects.filter(user=request.user)  # Filter tasks to include only those belonging to the user
        serializer = TaskSerializer(tasks, many=True)  # Serialize the task data for response
        return Response(serializer.data)  # Return serialized data in the response

    def retrieve(self, request, pk=None):
        """
        Retrieve a specific task by ID.
        """
        task = self.get_object(pk)  # Get the task object using its ID
        serializer = TaskSerializer(task)  # Serialize the task data
        return Response(serializer.data)  # Return serialized data in the response

    def create(self, request):
        """
        Create a new task for the authenticated user.
        """
        serializer = TaskSerializer(data=request.data)  # Initialize serializer with request data
        if serializer.is_valid():  # Validate the data
            serializer.save(user=request.user)  # Save the task with the authenticated user
            return Response(serializer.data, status=201)  # Return the created task data with 201 status
        return Response(serializer.errors, status=400)  # Return errors with 400 status if invalid
    def update(self, request, pk=None):
        """
        Update a specific category by ID.
        """
        task = self.get_object(pk)  # Get the task object to update
        serializer = TaskSerializer(task, data=request.data)  # Initialize serializer with request data
        if serializer.is_valid():  # Validate the updated data
            serializer.save()  # Return the updated task data
            return Response(serializer.data)  # Return the updated category data
        return Response(serializer.errors, status=400)  # Return errors if invalid


    def destroy(self, request, pk=None):
        """
        Delete a specific task by ID.
        """
        task = self.get_object(pk)  # Get the task object to delete
        task.delete()  # Delete the task
        return Response(status=204)  # Return a 204 No Content response

    def get_object(self, pk):
        """
        Helper method to retrieve a task by ID.
        Returns a 404 response if the task does not exist.
        """
        try:
            return Task.objects.get(pk=pk, user=self.request.user)  # Get the task for the authenticated user
        except Task.DoesNotExist:
            return Response(status=404)  # Return 404 if the task does not exist

    def send_notification(self, task):
        """
        Send a notification to the user regarding the task's due date.
        """
        Notification.objects.create(
            user=task.user,  # Associate the notification with the user of the task
            message=f'Task "{task.title}" is due on {task.due_date}.',  # Notification message
            task=task  # Link the notification to the specific task
        )