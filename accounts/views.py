"""
Note: 
- The 'login_view' function contains a placeholder comment '# future -> ?next=/articles/create/' which suggests a potential future enhancement to handle redirection after login.
- Assumes existence of corresponding HTML templates for registration, login, and logout.
"""

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm#, UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

#'register_view': Renders a registration form using UserCreationForm. Upon submission of valid form data, a new user is created and redirected to the homepage.

def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save(commit=False)
        user_obj.save()  
        login(request, user_obj)
        
        # Check if the user already has this ticker in their portfolio
        try:
            user = UserProfile.objects.get(user=user_obj)
        except UserProfile.DoesNotExist:
            user = UserProfile(user=user_obj, balance=0, buying_power=0)
        user.save()
        user_obj = form.save()
        return redirect('../login/')
    context = {"form": form}
    return render(request, "accounts/register.html", context)

#'login_view': Renders a login form using AuthenticationForm. If the form is submitted via POST with valid credentials, the user is logged in and redirected to the homepage.
def login_view(request):
    # future -> ?next=/articles/create/
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm(request)
    context = {
        "form": form
    }
    return render(request, "accounts/login.html", context)

#'logout_view': Logs out the user and redirects to the login page.
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login/")
    return render(request, "accounts/logout.html", {})