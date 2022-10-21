from django.urls import path
from users import views

urlpatterns = [
    path('student_form/', views.student_form),
    path('manager_form/', views.manager_form),
]