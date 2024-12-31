from django.urls import path
from mySecApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('forms/', views.forms_view, name='forms'),
]