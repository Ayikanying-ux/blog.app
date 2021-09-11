from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreateUser.as_view(), name='register'),
    path('login/', views.login_request, name ='login_request'),
    path('ajax/validate-username/', views.ValidateUsername.as_view(), name="validate-username")
]