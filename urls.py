from django.urls import path
from . import views

urlpatterns = [
    path('Views.py', views.home, name='home'),
    path('points/', views.points, name='points'),
]
