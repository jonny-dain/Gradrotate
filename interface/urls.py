from django.urls import path
from interface import views

urlpatterns = [
    path('', views.admin_interface),
    path('interns/', views.intern_interface),
    path('allocate/', views.allocate_interface),
    path('allocate/excel', views.allocate_excel),
    path('jobs/', views.job_interface),
    path('deleteIntern/<int:pk>/', views.deleteIntern, name='deleteIntern' ),
    path('deleteJob/<int:pk>/', views.deleteJob, name='deleteJob' )

]