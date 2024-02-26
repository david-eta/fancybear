from django.conf import settings
from django.db import models
from stocks.models import Stock
# Create your models here.

User = settings.AUTH_USER_MODEL

class Favorite(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    stock = models.CharField(primary_key=True, max_length=5)
    
    # make them composite keys
    class Meta:
        unique_together = ('user', 'stock')
