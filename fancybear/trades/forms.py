from django import forms
from django.core.exceptions import ValidationError
from .models import Trade
from stocks.models import Stock

class TradeForm(forms.ModelForm):
    ticker = forms.CharField(max_length=10, required=True)  # Add a ticker field

    class Meta:
        model = Trade
        fields = ['ticker', 'quantity', 'date', 'time', 'action']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # This will use HTML5 date picker
            'time': forms.TimeInput(attrs={'type': 'time'}),  # This will use HTML5 time picker
        } 

    def clean_ticker(self):
        ticker = self.cleaned_data['ticker']
        try:
            stock = Stock.objects.get(ticker=ticker)
        except Stock.DoesNotExist:
            raise ValidationError("Stock with this ticker does not exist")
        return stock  # Return the Stock object, not the ticker string

    def save(self, commit=True):
        instance = super(TradeForm, self).save(commit=False)
        instance.stock = self.cleaned_data['ticker']  # 'ticker' is now a Stock object
        if commit:
            instance.save()
        return instance
