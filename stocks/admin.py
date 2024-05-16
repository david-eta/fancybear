"""
Functionality:
- Registers the 'Stock' model with the Django admin interface to enable CRUD operations on Stock objects through the admin panel.

Note:
- Assumes the existence of the 'Stock' model in the same directory as the admin.py file.
- Allows administrators to manage Stock objects via the Django admin interface.
"""

from django.contrib import admin
from .models import Stock
# Register your models here.
admin.site.register(Stock)