from django.db import models

# Create your models here.
class Stock(models.Model):
    ticker = models.CharField(primary_key=True, max_length=5)
    name = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.TextField()