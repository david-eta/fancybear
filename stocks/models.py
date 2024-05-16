"""
Functionality:
- Defines the 'Stock' model representing a stock entity.

Attributes:
- 'ticker': CharField representing the ticker symbol of the stock. It serves as the primary key for the model and has a maximum length of 5 characters.
- 'name': TextField representing the name of the stock.
- 'price': DecimalField representing the price of the stock with a maximum of 12 digits and 2 decimal places.
- 'category': TextField representing the category of the stock.

Note:
- Each instance of the 'Stock' model represents a unique stock entity with its ticker symbol, name, price, and category.
- The 'ticker' attribute is specified as the primary key, indicating that each stock should have a unique ticker symbol.
"""
from django.db import models

# Create your models here.
class Stock(models.Model):
    ticker = models.CharField(primary_key=True, max_length=5)
    name = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.TextField()