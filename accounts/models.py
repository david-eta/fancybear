from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model() 

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    buying_power = models.DecimalField(max_digits=12, decimal_places=2, default=0)