from django.db import models
from django.conf import settings
# Create your models here.


User = settings.AUTH_USER_MODEL

class Trade(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    quantity = models.DecimalField(max_digits=12, decimal_places=5)
    action   = models.CharField(
        max_length=4,
        choices=[
            ('BUY', 'Buy'),
            ('BUY', 'Sell'),
        ]
    )
    
    stock = models.CharField(max_length=5)
    date = models.DateTimeField(auto_now_add=True)

