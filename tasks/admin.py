from django.contrib import admin
from .models import Task

# ============================================
# ADMIN REGISTRATION
# ============================================
# This tells Django: "Show the Task model in the admin panel"
# So we can add, edit, and delete tasks through a web interface.
# ============================================


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """
    Customize how Tasks appear in the admin panel.
    """
    
    # Columns to show in the task list
    list_display = ['title', 'completed', 'created_at']
    
    # Add a filter sidebar to filter by completion status
    list_filter = ['completed', 'created_at']
    
    # Add a search box to search by title
    search_fields = ['title']
    
    # Allow clicking on completed checkbox directly in the list
    list_editable = ['completed']
