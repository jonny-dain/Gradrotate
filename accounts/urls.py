from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.login),
    path('register/', views.register, name="register"),
    path('login/', views.login, name = "login"),
    path('logout/', views.logout, name = "logout"),
]