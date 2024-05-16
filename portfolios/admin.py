"""
Functionality:
- Registers the 'Portfolio' model with the Django admin interface to enable CRUD operations on Portfolio objects through the admin panel.

Note:
- Assumes the existence of the 'Portfolio' model in the same directory as the admin.py file.
- Allows administrators to manage Portfolio objects via the Django admin interface.
"""

from django.contrib import admin
from .models import Portfolio
# Register your models here.
admin.site.register(Portfolio)