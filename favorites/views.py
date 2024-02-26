import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Favorite
# Create your views here.

@login_required
def favorites_view(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'favorites.html', {'favorites': favorites})

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
