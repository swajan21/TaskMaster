from django.contrib import admin
from .models import Task


# Registering Task model with Django admin using a custom admin interface
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    # Fields to display as columns in the admin task list view
    list_display = ('title', 'user', 'due_date', 'priority', 'completed', 'is_overdue')

    # Fields to filter by (adds sidebar filters in admin)
    list_filter = ('priority', 'completed', 'due_date')

    # Enable search by these fields
    search_fields = ('title', 'description')

    # Default ordering (newest due date first)
    ordering = ('-due_date',)