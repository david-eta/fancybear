"""
Functionality:
1. 'Feedback': A model class representing user feedback. It contains fields for name, email, and feedback text. The '__str__' method is overridden to return the name of the feedback submitter.

2. 'BugReport': A model class representing bug reports. It contains fields for name, email, and bug description. The '__str__' method is overridden to return the name of the bug reporter.

Note:
- The models are defined using Django's 'models.Model' class and various field types such as 'CharField', 'EmailField', and 'TextField'.
- '__str__' methods are implemented to provide a human-readable representation of model instances.
- Make sure these models are registered in the Django admin or utilized appropriately within the Django application.
"""

# models.py

from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    feedback = models.TextField()

    def __str__(self):
        return self.name

class BugReport(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bug_description = models.TextField()

    def __str__(self):
        return self.name