from django.shortcuts import render, redirect
from .forms import SearchForm, StockForm
from .apihandler import stock_details, search_results
from django.contrib.auth.decorators import login_required
from portfolios.models import Portfolio
from trades.models import Trade
from django.http import HttpResponse 
from favorites.models import Favorite
# Create your views here.

def search_results_view(request):
    results = []
    
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = search_results(query)
    else:
        form = SearchForm()

    if request.user.is_authenticated:
        favorites = set(Favorite.objects.filter(user=request.user).values_list('stock', flat=True))
    else:
        favorites = set()
       
    context =  {'form': form, 
                'results': results, 
                'search_query': query,
                'favorites': favorites
                }
    return render(request, 'stocks/search_results.html', context=context)


def stock_details_view(request, ticker):
    details = stock_details(ticker)  # Get stock details for the given ticker
    return render(request, 'stocks/stock_details.html', {'details': details, 'ticker': ticker})


@login_required
def add_trade_view(request):
    form = StockForm()
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            action = form.cleaned_data['action']
            quantity = form.cleaned_data['quantity']
            ticker = form.cleaned_data['ticker'].upper()  # Ensure ticker is uppercase for consistency

            # Get the current price of the ticker
            ticker_price = stock_details(ticker)['price']
            if ticker_price is None:
                return HttpResponse("Ticker price could not be fetched.", status=400)

            # Check if the user already has this ticker in their portfolio
            try:
                portfolio = Portfolio.objects.get(user=request.user, stock=ticker)
            except Portfolio.DoesNotExist:
                if action == 'SELL':
                    return HttpResponse("Cannot sell a stock not in portfolio.", status=400)
                portfolio = Portfolio(user=request.user, stock=ticker, quantity=0, value=0)
            
            if action == 'BUY':
                portfolio.quantity += quantity
                portfolio.value += quantity * ticker_price
            elif action == 'SELL':
                if portfolio.quantity < quantity:
                    return HttpResponse("Cannot sell more than you own.", status=400)
                portfolio.quantity -= quantity
                portfolio.value -= quantity * ticker_price
            
            portfolio.save()

            # add to trade history
            trade = Trade(
                user=request.user,
                quantity=quantity,
                action=action,
                stock=ticker,
            )
            trade.save()
            return redirect('portfolio')  # Redirect to the portfolio page or another appropriate page

    return render(request, 'stocks/add_trade.html', {'form': form})
