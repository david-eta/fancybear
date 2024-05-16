"""
Functionality:
1. 'FeedbackForm': A form class that allows users to submit feedback. It renders fields for name, email, and feedback text. It is associated with the Feedback model and accepts input for the 'name', 'email', and 'feedback' fields.

2. 'BugReportForm': A form class for submitting bug reports. It renders fields for name, email, and bug description. It is associated with the BugReport model and accepts input for the 'name', 'email', and 'bug_description' fields.

Note:
- Assumes the existence of corresponding models (Feedback and BugReport) in the application.
- Ensure that the 'models.py' file contains the necessary models for this form to function correctly.
"""
# forms.py

from django import forms
from .models import *  # Make sure you have a Feedback model in your models.py

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'feedback']
        
class BugReportForm(forms.ModelForm):
    class Meta:
        model = BugReport
        fields = ['name', 'email', 'bug_description']