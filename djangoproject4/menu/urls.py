from django.urls import path

from .views import base

urlpatterns = [
    path('home/', base, {'name': 'Home'}, name='home'),
    path('<str:url>', base, {'name': 'Home'}, name='home'),
]
