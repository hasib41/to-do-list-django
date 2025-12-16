from django.db import models

# ============================================
# TASK MODEL
# ============================================
# This is like a blueprint for our database table.
# Each "class" becomes a TABLE in the database.
# Each "field" becomes a COLUMN in that table.
# ============================================


class Task(models.Model):
    """
    A Task represents one to-do item in our list.
    
    Database table will look like:
    +----+------------------+-----------+---------------------+
    | id | title            | completed | created_at          |
    +----+------------------+-----------+---------------------+
    | 1  | Buy groceries    | False     | 2024-12-16 10:00:00 |
    | 2  | Finish homework  | True      | 2024-12-16 11:30:00 |
    +----+------------------+-----------+---------------------+
    """
    
    # FIELD 1: title
    # - CharField = short text (like a text input in a form)
    # - max_length = maximum number of characters allowed
    # - This stores the name of the task, e.g., "Buy groceries"
    title = models.CharField(max_length=200)
    
    # FIELD 2: completed
    # - BooleanField = True or False (checkbox)
    # - default=False = new tasks start as "not completed"
    # - This tracks whether the task is done or not
    completed = models.BooleanField(default=False)
    
    # FIELD 3: created_at
    # - DateTimeField = date and time
    # - auto_now_add=True = automatically set to current time when created
    # - This records when the task was created
    created_at = models.DateTimeField(auto_now_add=True)
    
    # ============================================
    # SPECIAL METHODS
    # ============================================
    
    def __str__(self):
        """
        This method defines what to show when we print a Task.
        Without this: <Task object (1)>
        With this:    "Buy groceries"
        
        Used in admin panel and debugging.
        """
        return self.title
    
    class Meta:
        """
        Meta options for this model.
        - ordering: default order when fetching tasks from database
        - '-created_at' means newest first (the minus sign = descending)
        """
        ordering = ['-created_at']
