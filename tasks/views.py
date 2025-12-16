from django.shortcuts import render
from .models import Task

# ============================================
# VIEWS - Functions that return web pages
# ============================================
# A VIEW is a Python function that:
# 1. Receives a REQUEST (user asking for a page)
# 2. Does some work (get data, process forms, etc.)
# 3. Returns a RESPONSE (usually an HTML page)
# ============================================


def task_list(request):
    """
    VIEW: Show all tasks to the user.
    
    URL: / (homepage)
    
    How it works:
    1. User visits the website
    2. Django calls this function
    3. We get all tasks from database
    4. We put tasks into an HTML template
    5. We send the HTML back to the user
    
    Parameters:
    -----------
    request : HttpRequest
        Contains info about the user's request:
        - request.method → 'GET' or 'POST'
        - request.user → who is logged in
        - request.GET → URL parameters
        - request.POST → form data
    
    Returns:
    --------
    HttpResponse
        An HTML page showing all tasks
    """
    
    # STEP 1: Get all tasks from database
    # Task.objects.all() returns a QuerySet (like a list) of all Task objects
    # Remember: We set ordering = ['-created_at'] in model, so newest first!
    tasks = Task.objects.all()
    
    # STEP 2: Create a "context" dictionary
    # This sends data to the HTML template
    # Key 'tasks' will be available in the template as {{ tasks }}
    context = {
        'tasks': tasks,
    }
    
    # STEP 3: Render the template with the data
    # render() combines:
    #   - The request
    #   - Template file name ('tasks/task_list.html')
    #   - Context data (our tasks)
    # And returns a complete HTML page!
    return render(request, 'tasks/task_list.html', context)
