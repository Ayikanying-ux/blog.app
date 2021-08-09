from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreateUser, name='register'),
    path('login/', views.login_request, name ='login_request')
]