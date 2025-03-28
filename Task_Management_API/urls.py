"""
URL configuration for task_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin  # Import the admin module to access the Django admin site
from django.urls import path, include  # Import path and include functions for URL routing
from django.views.generic import TemplateView

urlpatterns = [
    # URL pattern for the API documentation page
    path('', TemplateView.as_view(template_name='tasks/documentation.html'), name='api-documentation'),
    # This maps the root URL to the API documentation template

    # URL pattern for the Django admin site
    path('admin/', admin.site.urls),  # Maps the 'admin/' URL to the Django admin interface

    # URL patterns for the API endpoints
    path('api/accounts/', include('accounts.urls')),  # Include URL patterns for user account management
    path('api/categories/', include('categories.urls')),  # Include URL patterns for category management
    path('api/tasks/', include('tasks.urls')),  # Include URL patterns for task management
    path('api/history/', include('task_history.urls')),  # Include URL patterns for task history management
    path('api/notifications/', include('notifications.urls')),  # Include URL patterns for notification management
]