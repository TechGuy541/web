from django.urls import path
from . import views

app_name = 'compatibility'

urlpatterns = [
    path('', views.home, name='home'),
    path('request/', views.request_game_entry, name='request'),
]