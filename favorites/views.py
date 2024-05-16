"""
Note:
- These views require the user to be logged in ('@login_required') to access them.
- 'toggle_favorite' and 'remove_favorite' views are decorated with '@require_POST', ensuring that they only respond to POST requests.
- Utilizes Django's 'JsonResponse' to send JSON responses.
- JSON data is expected in the request body for 'toggle_favorite' and 'remove_favorite' views.
"""
import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Favorite

# Create your views here.
#'favorites_view': Renders the 'favorites.html' template with a list of favorites associated with the logged-in user.
@login_required
def favorites_view(request):
    favorites = Favorite.objects.filter(user=request.user)
    
    return render(request, 'favorites.html', {'favorites': favorites})
#'toggle_favorite': Toggles the favorite status of a stock for the logged-in user. Expects a POST request with JSON data containing the 'ticker' of the stock and its 'favorited' status. If the stock is already favorited, it removes it from favorites; otherwise, it adds it to favorites.
@login_required
@require_POST
def toggle_favorite(request):
    data = json.loads(request.body)
    ticker = data.get('ticker')
    favorited = data.get('favorited')

    obj, created = Favorite.objects.get_or_create(user=request.user, stock=ticker)
    if not created:# and not favorited:
        obj.delete()
        return JsonResponse({'success': True})
    
    return JsonResponse({'success': created or not favorited})
#'remove_favorite': Removes a stock from the favorites list of the logged-in user. Expects a POST request with JSON data containing the 'stock' to be removed. If the stock exists in the user's favorites, it is deleted; otherwise, it returns a failure response.
@login_required
@require_POST
def remove_favorite(request):
    data = json.loads(request.body)
    stock = data.get('stock')
    print(stock)
    user = request.user
    
    success = False
    try:
        favorite = Favorite.objects.get(user=user, stock=stock)
        favorite.delete()
        success = True
    except Favorite.DoesNotExist:
        success = False
    
    return JsonResponse({'success': success})
