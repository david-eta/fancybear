from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Search')


class StockForm(forms.Form):
    ACTION_CHOICES = [
        ('BUY', 'Buy',),
        ('SELL', 'Sell',),
    ]

    ticker = forms.CharField(max_length=5, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ticker symbol (e.g., AAPL)'
    }))
    quantity = forms.DecimalField(
        max_digits=12, 
        decimal_places=5, 
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Quantity'
        })
    )
    action = forms.ChoiceField(choices=ACTION_CHOICES, widget=forms.RadioSelect)

    # date = forms.DateField(widget=forms.SelectDateWidget)
    # time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
