from django.urls import path
from interface import views

urlpatterns = [
    path('', views.admin_interface),
    path('deleteIntern/<int:pk>/', views.deleteIntern, name='deleteIntern' )
]