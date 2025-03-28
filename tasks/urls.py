from django.urls import path  # Import the path function to define URL patterns
from .views import TaskViewSet  # Import the TaskViewSet to map URLs to view functions

urlpatterns = [
    # URL pattern for creating a new task
    path('create/', TaskViewSet.as_view({'post': 'create'}), name='task-create'),
    # This maps the POST request to the create method of TaskViewSet

    # URL pattern for listing all tasks
    path('list/', TaskViewSet.as_view({'get': 'list'}), name='task-list'),
    # This maps the GET request to the list method of TaskViewSet

    # URL pattern for retrieving a specific task by ID
    path('<int:pk>/', TaskViewSet.as_view({'get': 'retrieve'}), name='task-detail'),
    # This maps the GET request with a task ID to the retrieve method of TaskViewSet

    # URL pattern for updating a specific task by ID
    path('<int:pk>/update/', TaskViewSet.as_view({'put': 'update'}), name='task-update'),
    # This maps the PUT request with a task ID to the update method of TaskViewSet

    # URL pattern for deleting a specific task by ID
    path('<int:pk>/delete/', TaskViewSet.as_view({'delete': 'destroy'}), name='task-delete'),
    # This maps the DELETE request with a task ID to the destroy method of TaskViewSet
]