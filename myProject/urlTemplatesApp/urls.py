from django.urls import path
from urlTemplatesApp import views

app_name = "urlTemplatesApp"

urlpatterns = [
    path('base/', views.base, name='base'),
    path('relative/', views.relative, name='relative'),
]