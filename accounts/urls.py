from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.login),
    path('register/', views.register),
    path('login/', views.login),
]