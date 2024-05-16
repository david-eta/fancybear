"""
Functionality:
- 'Portfolio': Model representing a user's portfolio of stocks. It contains fields for user (ForeignKey), stock ticker, quantity of shares, average price, current price, and calculated values such as total investment, current value, gains, and return on investment (ROI).


Note:
- Uses settings.AUTH_USER_MODEL to reference the custom user model specified in the Django settings.
- 'total_investment', 'current_value', 'gains', and 'roi' fields are calculated based on other fields and are marked as 'editable=False' to prevent direct editing in the Django admin.
- The 'Meta' class defines 'unique_together' to enforce uniqueness constraint on the combination of 'user' and 'stock'.
"""

from django.conf import settings
from django.db import models
# Create your models here.

User = settings.AUTH_USER_MODEL

class Portfolio(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    stock = models.CharField(max_length=5)
    quantity = models.DecimalField(max_digits=12, decimal_places=5) # num of shares
    
    average_price = models.DecimalField(max_digits=10, decimal_places=2, default=0) # changes when stocks are bought
    current_price = models.DecimalField(max_digits=10, decimal_places=2, default=0) # will change in real time
    
    # Fields for calculated values
    # editable=False makes sure these values can't be edited in django admin
    total_investment = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)
    current_value = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)
    gains = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)
    roi = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)
    #initial_deposit = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)
    
    #'save' method: Overrides the default save method to update calculated fields (total_investment, current_value, gains, and ROI) before saving the object.
    def save(self, *args, **kwargs):
        # Update calculated fields before saving
        self.total_investment = self.average_price * self.quantity
        self.current_value = self.current_price * self.quantity
        self.gains = self.current_value - self.total_investment
        self.roi = (self.gains / self.total_investment) * 100 if self.total_investment != 0 else 0

        super().save(*args, **kwargs)

    
    # make them composite keys
    class Meta:
        unique_together = ('user', 'stock')
    
