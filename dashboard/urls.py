from django.urls import path
from dashboard import views

urlpatterns = [
    path('', views.preference),
    path('sort/', views.sort, name = 'sort'),
]