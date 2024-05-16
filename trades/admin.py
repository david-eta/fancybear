"""
Registers the Trade model with the Django admin site.

Dependencies:
    - django.contrib.admin: Module for configuring the Django admin interface.
    - .models: Module containing the Trade model.

"""

from django.contrib import admin
from .models import Trade
# Register your models here.
admin.site.register(Trade)