"""
Functionality:
1. 'Favorite': Model representing the favorites of users. It has a ForeignKey to the User model (settings.AUTH_USER_MODEL) and a CharField for the stock's ticker. The combination of 'user' and 'stock' fields forms a composite primary key.

Note:
- Uses settings.AUTH_USER_MODEL to reference the custom user model specified in the Django settings.
- The 'user' field allows null values and is set to null on user deletion ('on_delete=models.SET_NULL').
- 'stock' field is the primary key of the Favorite model and represents the ticker symbol of the stock.
- The 'Meta' class defines 'unique_together' to enforce uniqueness constraint on the combination of 'user' and 'stock'.
"""
from django.conf import settings
from django.db import models
# Create your models here.

User = settings.AUTH_USER_MODEL

class Favorite(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    stock = models.CharField(primary_key=True, max_length=5)
    
    # make them composite keys
    class Meta:
        unique_together = ('user', 'stock')
