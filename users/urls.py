from django.urls import path
from users import views

urlpatterns = [
    path('student_form/', views.student_form),
    path('student_form/requirements',views.student_form_requirements, name= 'student_form_requirements'),
    path('student_form/skills',views.student_form_skills),
    path('manager_form/', views.manager_form),
    path('manager_form/information', views.manager_form_requirements),
    path('manager_form/information_2', views.manager_form_additional_requirements),
    path('manager_form/skills', views.manager_form_skills),
    path('student_form/complete', views.student_complete),
    path('manager_form/complete', views.manager_complete),


]