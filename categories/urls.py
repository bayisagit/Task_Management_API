from django.urls import path  # Import the path function to define URL patterns
from .views import CategoryViewSet  # Import the CategoryViewSet to map URLs to view functions

urlpatterns = [
    # URL pattern for creating a new category
    path('create/', CategoryViewSet.as_view({'post': 'create'}), name='category-create'),
    # This maps the POST request to the create method of CategoryViewSet

    # URL pattern for listing all categories
    path('list/', CategoryViewSet.as_view({'get': 'list'}), name='category-list'),
    # This maps the GET request to the list method of CategoryViewSet

    # URL pattern for retrieving a specific category by ID
    path('<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve'}), name='category-detail'),
    # This maps the GET request with a category ID to the retrieve method of CategoryViewSet

    # URL pattern for updating a specific category by ID
    path('<int:pk>/update/', CategoryViewSet.as_view({'put': 'update'}), name='category-update'),
    # This maps the PUT request with a category ID to the update method of CategoryViewSet

    # URL pattern for deleting a specific category by ID
    path('<int:pk>/delete/', CategoryViewSet.as_view({'delete': 'destroy'}), name='category-delete'),
    # This maps the DELETE request with a category ID to the destroy method of CategoryViewSet
]