"""
Functionality:



Note:
- These views require the user to be logged in ('@login_required') to access them.
- 'remove_portfolio' view is decorated with '@require_POST', ensuring that it only responds to POST requests.
- 'update_stock_info' view utilizes an external method 'stock_details' to fetch the latest price of the stock and calculates other values based on business logic.
- Utilizes Django's 'JsonResponse' to send JSON responses.
"""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Portfolio
import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from trades.models import Trade
import datetime
from stocks.apihandler import stock_details
from accounts.models import UserProfile
# Create your views here.

#'portfolio_view': Renders the 'portfolio.html' template with a list of portfolios associated with the logged-in user.
@login_required
def portfolio_view(request):
    user = UserProfile.objects.get(user=request.user)
    print(user.balance)
    portfolios = Portfolio.objects.filter(user=request.user)
    return render(request, 'portfolio.html', {'portfolios': portfolios, 'user_balance': user.balance})

#'remove_portfolio': Removes a stock from the user's portfolio. Expects a POST request with JSON data containing the 'stock' to be removed. It also adds a 'sell trade' to the trade history.
@login_required
@require_POST
def remove_portfolio(request):
    data = json.loads(request.body)
    stock = data.get('stock')
    print(stock)
    
    success = False
    try:
        portfolio = Portfolio.objects.get(user=request.user, stock=stock)
        user = UserProfile.objects.get(user=request.user)
        user.buying_power += portfolio.current_value
        user.save()
        # adds a 'sell trade' to trade history
        trade = Trade(
            user=request.user,
            quantity=portfolio.quantity,
            action="SELL",
            stock=portfolio.stock,
            value=portfolio.value,#There is no value attribute, total investment?
            date=datetime.date.today(),
        )
        trade.save()
        portfolio.delete() # deletes from portfolio
        
        success = True
    except Portfolio.DoesNotExist:
        success = False
    
    return JsonResponse({'success': success})

#'update_stock_info': Retrieves updated stock information (current price, current value, gains, and ROI) for a given stock ticker. Expects a GET request with the ticker parameter.
@login_required
def update_stock_info(request):
     
    ticker = request.GET.get('ticker')
    if ticker:
        try:
            # Assuming stock_details(ticker) returns the latest price and you have all necessary methods to calculate other values
            current_price = stock_details(ticker)['price']
            portfolio = Portfolio.objects.get(user=request.user, stock=ticker)
            user = UserProfile.objects.get(user=request.user)
            current_value = current_price * portfolio.quantity
            # Calculate gains and ROI based on your business logic
            gains = current_value - (portfolio.average_price * portfolio.quantity)
            roi = (gains / (portfolio.average_price * portfolio.quantity)) * 100
            user.balance += gains

            response = {
                'current_price': current_price,
                'current_value': current_value,
                'gains': gains,
                'roi': roi,
                'user_balance': user.balance,
            }
            user.save()
            return JsonResponse(response)
        except Portfolio.DoesNotExist:
            return JsonResponse({'error': 'Portfolio item does not exist'}, status=404)
    return JsonResponse({'error': 'No ticker provided'}, status=400)