"""
URL configuration for fancybear project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from portfolios.views import *
from accounts.views import *
from stocks.views import *
from favorites.views import *
from trades.views import *
from .views import *

urlpatterns = [
    path('', home_view, name="home"), # index / home / root 
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('add_trade/', add_trade_view, name='add_trade'),
    path('trade_history/', history_view, name='trade_history'),
    path('portfolio/', portfolio_view, name='portfolio'),
    path('about_us/', aboutUs_view, name='about'),
    path('contact_us/', contactUs_view, name='contact'),
    path('report_bug/', reportBug_view, name='report'),
    path('search_stock/', search_results_view, name='search_results'),
    path('stock-details/<str:ticker>/', stock_details_view, name='stock_details'),
    path('favorites/', favorites_view, name='favorites'),
    path('toggle_favorite/', toggle_favorite, name='toggle_favorite'),
    path('remove_favorite/', remove_favorite, name='remove_favorite'),
    path('remove_portfolio/', remove_portfolio, name='remove_portfolio'),
    
]