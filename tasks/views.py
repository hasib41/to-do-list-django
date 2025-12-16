from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# ============================================
# VIEWS - Functions that handle web requests
# ============================================


def task_list(request):
    """
    VIEW: Show all tasks AND handle adding new tasks.
    
    URL: / (homepage)
    
    This view handles TWO things:
    1. GET request  → Show the task list page
    2. POST request → Create a new task from form data
    
    This is a common pattern in Django!
    """
    
    # Check if user submitted the form (POST request)
    if request.method == 'POST':
        # Create a form with the submitted data
        form = TaskForm(request.POST)
        
        # Check if the data is valid
        if form.is_valid():
            # Save the new task to database
            form.save()
            
            # Redirect to the same page (prevents double submission)
            # redirect() sends user to a different URL
            return redirect('tasks:task_list')
    else:
        # GET request - just show empty form
        form = TaskForm()
    
    # Get all tasks from database
    tasks = Task.objects.all()
    
    # Send both tasks and form to template
    context = {
        'tasks': tasks,
        'form': form,
    }
    
    return render(request, 'tasks/task_list.html', context)


def toggle_complete(request, task_id):
    """
    VIEW: Toggle a task's completed status.
    
    URL: /toggle/<task_id>/
    
    How it works:
    1. Get the task by its ID
    2. Flip the 'completed' value (True → False, False → True)
    3. Save the task
    4. Redirect back to task list
    
    Parameters:
    -----------
    task_id : int
        The ID of the task to toggle (comes from URL)
    """
    
    # get_object_or_404: Get the task OR show 404 error if not found
    task = get_object_or_404(Task, id=task_id)
    
    # Toggle the completed status
    # If True → becomes False
    # If False → becomes True
    task.completed = not task.completed
    
    # Save the change to database
    task.save()
    
    # Redirect back to task list
    return redirect('tasks:task_list')


def delete_task(request, task_id):
    """
    VIEW: Delete a task.
    
    URL: /delete/<task_id>/
    
    How it works:
    1. Get the task by its ID
    2. Delete it from database
    3. Redirect back to task list
    
    Parameters:
    -----------
    task_id : int
        The ID of the task to delete (comes from URL)
    """
    
    # Get the task or show 404 if not found
    task = get_object_or_404(Task, id=task_id)
    
    # Delete the task from database
    task.delete()
    
    # Redirect back to task list
    return redirect('tasks:task_list')
