from django.urls import path
from users import views

urlpatterns = [
    
    path('student_form/', views.student_form, name = "student_form"),
    path('student_form/requirements',views.student_form_requirements, name= 'student_form_requirements'),
    path('student_form/skills',views.student_form_skills, name= 'student_form_skills'),
    path('student_form/complete', views.student_complete, name= 'student_complete'),
    path('student_form/allocation/complete', views.student_allocation_complete, name= 'student_allocation_complete'),




    path('<int:pk>/manager_form/', views.manager_form, name='managerForm'),
    path('<int:pk>/manager_form/information', views.manager_form_requirements, name='managerForm2'),
    path('<int:pk>/manager_form/information_2', views.manager_form_additional_requirements, name='managerForm3'),
    path('<int:pk>/manager_form/skills', views.manager_form_skills, name='managerForm4'),
    path('<int:pk>/manager_form/complete', views.manager_complete, name='managerForm5'),
    path('manager_form/allocation/complete', views.manager_allocation_complete, name='manager_allocation_complete'),
    path('manager_dashboard/',views.manager_dashboard, name='manager_dashboard'),
    path('manager_form/create_job/', views.manager_create_job, name='manager_create_job'),
    path('<int:pk>/manager_form/delete_job/', views.manager_delete_job, name='managerDeleteJob'),
    

]

app_name = 'users'