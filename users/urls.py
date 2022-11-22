from django.urls import path
from users import views

urlpatterns = [
    path('student_form/', views.student_form),
    path('student_form/requirements',views.student_form_requirements),
    path('student_form/skills',views.student_form_skills),
    path('manager_form/', views.manager_form),
    path('manager_form/requirements', views.manager_form_requirements),
    path('manager_form/skills', views.manager_form_skills),




]