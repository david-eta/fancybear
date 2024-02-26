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