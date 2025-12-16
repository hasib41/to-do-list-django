from django.urls import path
from . import views

# ============================================
# URL PATTERNS for the Tasks App
# ============================================

app_name = 'tasks'

urlpatterns = [
    # Homepage - show all tasks + add form
    # URL: /
    path('', views.task_list, name='task_list'),
    
    # Toggle task completion
    # URL: /toggle/1/ (for task with id=1)
    # <int:task_id> captures a number from the URL
    path('toggle/<int:task_id>/', views.toggle_complete, name='toggle_complete'),
    
    # Delete a task
    # URL: /delete/1/ (for task with id=1)
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
