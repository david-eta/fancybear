"""
Functionality:
- Registers the 'Favorite' model with the Django admin interface to enable CRUD operations on Favorite objects through the admin panel.

Note:
- Assumes the existence of the 'Favorite' model in the same directory as the admin.py file.
- Allows administrators to manage Favorite objects via the Django admin interface.
"""
from django.contrib import admin
from .models import Favorite

admin.site.register(Favorite)