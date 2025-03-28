from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'user', 'status')  # Customize fields displayed in the list view
    actions = ['send_notifications']  # Add custom admin actions

    def send_notifications(self, request, queryset):
        """
        Custom admin action to send notifications for selected tasks.
        """
        for task in queryset:
            self.send_notification(task)
        self.message_user(request, "Notifications sent successfully!")  # Provide feedback in admin UI

    def send_notification(self, task):
        """
        Logic to send notifications (similar to your ViewSet method).
        """
        from notifications.models import Notification
        Notification.objects.create(
            user=task.user,
            message=f'Task "{task.title}" is due on {task.due_date}.',
            task=task
        )

    send_notifications.short_description = "Send notifications for selected tasks"

admin.site.register(Task, TaskAdmin)