from django.urls import path
from interface import views



urlpatterns = [
    path('', views.admin_interface),
    path('interns/', views.intern_interface),
    path('allocate/', views.allocate_interface),
    path('allocate/excel', views.allocate_excel),
    path('jobs/', views.job_interface),
    path('deleteIntern/<int:pk>/', views.deleteIntern, name='deleteIntern' ),
    path('deleteJob/<int:pk>/', views.deleteJob, name='deleteJob' ),
    path('deleteOffice/<int:pk>/', views.deleteOffice, name='deleteOffice' ),
    path('deleteSkillComputing/<int:pk>/', views.deleteSkillComputing, name='deleteSkillComputing' ),
    path('deleteSkillAnalytic/<int:pk>/', views.deleteSkillAnalytic, name='deleteSkillAnalytic' ),
    path('deleteSkillMarketing/<int:pk>/', views.deleteSkillMarketing, name='deleteSkillMarketing' ),
    path('deleteSkillManagement/<int:pk>/', views.deleteSkillManagement, name='deleteSkillManagement' ),
    path('deleteSkillLeadership/<int:pk>/', views.deleteSkillLeadership, name='deleteSkillLeadership' ),
    path('deleteSkillBusiness/<int:pk>/', views.deleteSkillBusiness, name='deleteSkillBusiness' ),
    path('deleteSkillAdmin/<int:pk>/', views.deleteSkillAdmin, name='deleteSkillAdmin' ),
]