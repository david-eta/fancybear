from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Portfolio
import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
# Create your views here.

@login_required
def portfolio_view(request):
    portfolios = Portfolio.objects.filter(user=request.user)#.annotate(stock_value=F('quantity') * Sum('stock__price'))
    return render(request, 'portfolio.html', {'portfolios': portfolios})

@login_required
@require_POST
def remove_portfolio(request):
    data = json.loads(request.body)
    stock = data.get('stock')
    print(stock)
    user = request.user
    
    success = False
    try:
        portfolio = Portfolio.objects.get(user=user, stock=stock)
        portfolio.delete()
        success = True
    except Portfolio.DoesNotExist:
        success = False
    
    return JsonResponse({'success': success})
