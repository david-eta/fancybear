'''
Functionality:
This AppConfig class defines the configuration for the 'accounts' app.
It sets the default_auto_field attribute to 'django.db.models.BigAutoField'.
It specifies the name of the app as 'accounts'.
'''
from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
