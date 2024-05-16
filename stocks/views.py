"""
This module contains views for managing stocks in the application.

Dependencies:
    - Django: The web framework used for the application.
    - django.shortcuts: Utility functions for rendering templates and redirecting requests.
    - .forms: Module containing forms used in the application.
    - .apihandler: Module containing functions to interact with external APIs for stock data.
    - django.contrib.auth.decorators: Decorators for controlling access to views based on authentication.
    - portfolios.models: Models for managing user portfolios.
    - trades.models: Models for managing user trades.
    - django.utils.timezone: Utilities for handling time-related operations.
    - favorites.models: Models for managing user favorite stocks.
    - datetime: Module for manipulating dates and times.
    - django.http.JsonResponse: Class for returning JSON-encoded responses.

"""

from django.shortcuts import render, redirect
from .forms import SearchForm, StockForm, BalanceForm
from .apihandler import stock_details, search_results, historical_stock_price, get_chart_data
from django.contrib.auth.decorators import login_required
from portfolios.models import Portfolio
from accounts.models import UserProfile
from django.db.models import Sum
from trades.models import Trade
from django.utils import timezone
from favorites.models import Favorite
import datetime
from django.http import JsonResponse
import pandas as pd
from django.contrib import messages
# Create your views here.

#search_results_view: Renders the search results page with stock search functionality.
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

#stock_details_view: Renders the details page for a specific stock.
def stock_details_view(request, ticker):
    user_history = Trade.objects.filter(user=request.user,stock=ticker).order_by('-date')
    details = stock_details(ticker)  # Get stock details for the given ticker
    return render(request, 'stocks/stock_details.html', {'details': details, 'ticker': ticker, 'history': user_history})

#get_chart_prices: Retrieves chart data for a specific stock and time interval.
def get_chart_prices(request):
    ticker = request.GET.get('ticker')
    time_interval = request.GET.get('time_interval')  # Provide a default value
    print(ticker)
    print(time_interval)
    
    chart_data = get_chart_data(ticker, time_interval)
    return JsonResponse(chart_data)

#add_trade_view: Handles adding trades (buy/sell) for a specific stock.
@login_required
def add_trade_view(request, ticker):
    user = UserProfile.objects.get(user=request.user)
    ticker = ticker.upper()
    form = StockForm()
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            action = form.cleaned_data['action']
            quantity = form.cleaned_data['quantity']
            # Get today's date
            date = get_most_recent_business_day()
            
            
            
            details = stock_details(ticker)
            if details == {} or details == None:
                form.add_error(None, 'No stock with this ticker exists in our database.')
                return render(request, 'stocks/add_trade.html', {'buying_power': user.buying_power, 'form': form, 'ticker': ticker, 'error_message': form.non_field_errors()})
            ticker_price = details['price']
                
            # Check if the user already has this ticker in their portfolio
            try:
                portfolio = Portfolio.objects.get(user=request.user, stock=ticker)
            except Portfolio.DoesNotExist: # if it is not in the portfolio...
                if action == 'SELL':
                    form.add_error('action', 'You cannot sell a stock not in portfolio.')
                    return render(request, 'stocks/add_trade.html', {'buying_power': user.buying_power, 'form': form, 'ticker': ticker,})
                # create a record for it   
                portfolio = Portfolio(user=request.user, stock=ticker, quantity=0, average_price=0, gains=0)
                
            if action == 'BUY':
                if user.buying_power < (quantity * ticker_price):
                    form.add_error('quantity', f"You do not have enough buying power. You have {user.buying_power}. Try selling stocks you own or depositing more money.")
                    return render(request, 'stocks/add_trade.html', {'buying_power': user.buying_power, 'form': form, 'ticker': ticker,})
                portfolio.average_price = ((portfolio.average_price * portfolio.quantity) + (ticker_price * quantity)) / (portfolio.quantity+quantity)
                portfolio.quantity += quantity
                user.buying_power -= (quantity * ticker_price)
                user.save()
                
            elif action == 'SELL':
                # ensure that they do cannot sell more than they own
                if portfolio.quantity < quantity:
                    form.add_error('action', f"You cannot sell more than what you own. You own {portfolio.quantity} shares.")
                    return render(request, 'stocks/add_trade.html', {'buying_power': user.buying_power, 'form': form, 'ticker': ticker,})
                
                # delete from portfolio if they sell as much as they own
                elif portfolio.quantity == quantity:
                    portfolio.delete()
                
                # reduce from quantity accordingly if they sell less than they own
                else:
                    portfolio.quantity -= quantity
                    
                user.buying_power += (quantity * ticker_price)
                user.save()
                    
            portfolio.current_price = ticker_price
            portfolio.save()
            

            # add to trade history
            trade = Trade(
                user=request.user,
                quantity=quantity,
                action=action,
                stock=ticker,
                value=quantity*ticker_price,
                date=date,
            )
            trade.save()
            return redirect('portfolio')  # Redirect to the portfolio page or another appropriate page
    
    return render(request, 'stocks/add_trade.html', {'buying_power': user.buying_power, 'form': form, 'ticker': ticker,})

@login_required
def deposit_withdraw_view(request):
    user = UserProfile.objects.get(user=request.user)
    form = BalanceForm()
    if request.method == "POST":
        form = BalanceForm(request.POST)
        if form.is_valid():
            action = form.cleaned_data['action']
            quantity = form.cleaned_data['quantity']
            
            
            # Handle deposit
            if action.upper() == 'DEPOSIT':
                messages.success(request, 'This is a success notification because the condition was met!')
                user.balance += quantity
                user.buying_power += quantity
                
                user.save()

            # Handle withdraw
            elif action.upper() == 'WITHDRAW':
                if quantity <= user.balance:
                    if quantity <= user.buying_power:
                        user.balance -= quantity
                        user.buying_power -= quantity
                        user.save()
                    else:
                        form.add_error('quantity', f"You are not liquid enough. You can only withdraw {user.buying_power}. Try selling stocks you own.")
                        return render(request, 'stocks/deposit_withdraw.html', {'buying_power': user.buying_power, 'form': form})
                else:
                    form.add_error('quantity', f"You cannot withdraw more than your balance. You currently have {user.balance} in stocks and liquidity.")
                    return render(request, 'stocks/deposit_withdraw.html', {'buying_power': user.buying_power, 'form': form})
            print("balance",user.balance)
            return redirect('deposit_withdraw')  # Redirect to a success page or the same page to show status
    

    return render(request, 'stocks/deposit_withdraw.html', {'buying_power': user.buying_power, 'form': form})




# ---------------- HELPER FUNCTION(S) ------------------------
def get_most_recent_business_day():
    today = datetime.date.today()
    # If today is Saturday (5) or Sunday (6), subtract the appropriate number of days
    if today.weekday() == 5:  # Saturday
        return today - datetime.timedelta(days=1)
    elif today.weekday() == 6:  # Sunday
        return today - datetime.timedelta(days=2)
    else:
        # Check if today is a business day, if not get the last one
        if pd.bdate_range(end=today, periods=1)[0].date() != today:
            # pandas bdate_range gives us the previous business day if today is not one
            return pd.bdate_range(end=today, periods=1)[0].date()
        else:
            return today

# ---------------- HELPER FUNCTION(S) END ---------------------