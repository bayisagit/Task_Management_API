from rest_framework import viewsets, permissions  # Import viewsets and permissions from Django REST Framework
from .models import TaskHistory  # Import the TaskHistory model
from .serializers import TaskHistorySerializer  # Import the TaskHistory serializer

class TaskHistoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing task history entries.
    Provides functionality to list, create, retrieve, update, and delete task history entries.
    """
    serializer_class = TaskHistorySerializer  # Specify the serializer for the TaskHistory model
    permission_classes = [permissions.IsAuthenticated]  # Ensure that only authenticated users can access these endpoints

    def get_queryset(self):
        """
        Retrieve the task history entries for the authenticated user.
        """
        # Filter task history entries to only include those related to the user's tasks
        return TaskHistory.objects.filter(task__user=self.request.user)