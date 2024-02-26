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