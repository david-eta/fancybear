from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Trade

# Create your views here.
@login_required
def history_view(request):
    user_history = Trade.objects.filter(user=request.user).order_by('-date')
    return render(request, 'history.html', {'history': user_history})