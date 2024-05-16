"""
Defines the Trade model for managing user trades.

Attributes:
    - user: ForeignKey to the User model, representing the user who made the trade.
    - quantity: DecimalField representing the quantity of the traded stock.
    - value: DecimalField representing the value of the trade.
    - action: CharField representing the action of the trade (BUY or SELL).
    - stock: CharField representing the ticker symbol of the traded stock.
    - date: DateField representing the date of the trade.

Dependencies:
    - django.db.models: Module for defining Django models.
    - django.conf.settings: Module for accessing Django settings.
    - django.utils.timezone: Utilities for handling time-related operations.

"""

from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.


User = settings.AUTH_USER_MODEL

class Trade(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    quantity = models.DecimalField(max_digits=12, decimal_places=5)
    value = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    action   = models.CharField(
        max_length=4,
        choices=[
            ('BUY', 'Buy'),
            ('SELL', 'Sell'),
        ]
    )
    
    stock = models.CharField(max_length=5)
    date = models.DateField(auto_now_add=False, default=timezone.now)

