"""
Defines the configuration for the 'trades' app.

Attributes:
    - default_auto_field: Specifies the default primary key field for models in the app.
    - name: Specifies the name of the app.
"""

from django.apps import AppConfig


class TradesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'trades'
