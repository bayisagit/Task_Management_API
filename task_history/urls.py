from django.urls import path  # Import the path function to define URL patterns
from .views import TaskHistoryViewSet  # Import the TaskHistoryViewSet to map URLs to view functions

urlpatterns = [
    # URL pattern for listing task history entries
    path('', TaskHistoryViewSet.as_view({'get': 'list'}), name='task-history-list'),
    # This maps the root URL for task history to the list method of TaskHistoryViewSet
    # It allows authenticated users to retrieve their list of task history entries
]