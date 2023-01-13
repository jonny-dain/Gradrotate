from django.urls import path
from dashboard import views

urlpatterns = [
    path('', views.preference, name='preference'),
    path('sort/', views.sort, name = 'sort'),
]

app_name = 'dashboard'
