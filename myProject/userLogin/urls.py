from django.urls import path
from userLogin import views

app_name = 'userLogin'

urlpatterns = [
    path('', views.base, name='base'),
    path('index/', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
]