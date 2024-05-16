"""
Functionality:
- This 'PortfoliosConfig' class represents the configuration of the 'portfolios' app.

Note:
- 'default_auto_field' specifies the default primary key field type for models that don't have a primary key field explicitly defined. In this case, it's set to 'django.db.models.BigAutoField', which is suitable for large-scale applications.
- 'name' attribute specifies the name of the app, which is 'portfolios' in this case.
"""

from django.apps import AppConfig


class PortfoliosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolios'
