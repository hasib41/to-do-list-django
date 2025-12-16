from django import forms
from .models import Task

# ============================================
# DJANGO FORMS
# ============================================
# A Form handles:
# 1. Rendering HTML input fields
# 2. Validating user input
# 3. Cleaning/processing data
# ============================================


class TaskForm(forms.ModelForm):
    """
    A ModelForm automatically creates form fields
    based on the Task model.
    
    Instead of manually writing:
        title = forms.CharField()
        completed = forms.BooleanField()
    
    ModelForm does it for you based on the model!
    """
    
    class Meta:
        # Which model to base this form on
        model = Task
        
        # Which fields to include in the form
        # We only need 'title' because:
        # - 'completed' starts as False (default)
        # - 'created_at' is set automatically
        fields = ['title']
        
        # Customize the form widgets (HTML elements)
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'What needs to be done?',
                'autofocus': True,
            })
        }
