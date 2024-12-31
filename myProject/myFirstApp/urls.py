from django.urls import path
from myFirstApp import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('secondPage/', views.secondPage, name='secondPage'),
]