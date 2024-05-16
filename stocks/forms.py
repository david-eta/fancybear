"""
Functionality:
- 'get_most_recent_business_day': Helper function that returns the most recent business day. It checks if today is a weekend and adjusts accordingly. If today is not a business day, it retrieves the last business day using pandas' bdate_range.

- 'SearchForm': A form class representing a search form with a single field for user input. The user can enter a query to search.

- 'StockForm': A form class representing a form for buying or selling stocks. It includes fields for quantity, action (buy or sell), and date. The 'date' field is prepopulated with the most recent business day by default.

Note:
- The 'SearchForm' class is a basic form with a single text input field for search queries.
- The 'StockForm' class includes fields for quantity, action (buy or sell), and date. The 'date' field is prepopulated with the most recent business day using the 'get_most_recent_business_day' function.
- Some fields and attributes in the 'StockForm' class are commented out, indicating that they were part of the form but are no longer used.
- 'ACTION_CHOICES' defines the choices available for the 'action' field, which are 'BUY' and 'SELL'.
"""

from django import forms
import datetime

class SearchForm(forms.Form):
    query = forms.CharField(label='Search')


class StockForm(forms.Form):
    ACTION_CHOICES = [
        ('BUY', 'Buy',),
        ('SELL', 'Sell',),
    ]
    
    quantity = forms.DecimalField(
        required=True,
        min_value=0.00001,
        max_digits=12, 
        decimal_places=5, 
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Number of shares'
        })
    )
    
    action = forms.ChoiceField(required=True,choices=ACTION_CHOICES, widget=forms.RadioSelect)

    
class BalanceForm(forms.Form):
    ACTION_CHOICES = [
        ('Deposit', 'DEPOSIT',),
        ('Withdraw', 'WITHDRAW',),
    ]
    
    quantity = forms.DecimalField(
        required=True,
        label="Amount",
        min_value=1,
        max_digits=12, 
        decimal_places=2, 
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Amount in USD'
        })
    )
    
    action = forms.ChoiceField(label="Action",required=True,choices=ACTION_CHOICES, widget=forms.RadioSelect)
