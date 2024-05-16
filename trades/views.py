"""
Defines a view for displaying user trade history.

Attributes:
    - history_view: View function for rendering the user's trade history.

Dependencies:
    - django.shortcuts.render: Function for rendering templates.
    - django.contrib.auth.decorators.login_required: Decorator for restricting access to authenticated users.
    - .models.Trade: Trade model for retrieving user trade history.
"""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Trade

# Create your views here.
@login_required
def history_view(request):
    user_history = Trade.objects.filter(user=request.user).order_by('-date')
    return render(request, 'history.html', {'history': user_history})