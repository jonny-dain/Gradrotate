from django.urls import path
from interface import views

urlpatterns = [
    path('', views.admin_interface),
]