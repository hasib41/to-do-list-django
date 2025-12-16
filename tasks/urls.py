from django.urls import path
from . import views

# ============================================
# URL PATTERNS for the Tasks App
# ============================================
# This file maps URLs to views (functions)
# Like a phone book: URL → which function to call
# ============================================

# app_name is used for namespacing URLs
# So we can write: {% url 'tasks:task_list' %} in templates
app_name = 'tasks'

urlpatterns = [
    # Homepage - show all tasks
    # '' means empty path, so this is the root URL
    # views.task_list is the function to call
    # name='task_list' lets us reference this URL by name
    path('', views.task_list, name='task_list'),
]
