from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import *

class TestUrls(SimpleTestCase):

    #Intern
    def test_student_form_url_is_resolved(self):
        url = reverse('users:student_form')
        self.assertEquals(resolve(url).func, student_form)

    def test_student_form_requirements_url_is_resolved(self):
        url = reverse('users:student_form_requirements')
        self.assertEquals(resolve(url).func, student_form_requirements)
    
    def test_student_form_skills_url_is_resolved(self):
        url = reverse('users:student_form_skills')
        self.assertEquals(resolve(url).func, student_form_skills)
    
    def test_student_complete_url_is_resolved(self):
        url = reverse('users:student_complete')
        self.assertEquals(resolve(url).func, student_complete)
    
    def test_student_allocation_complete_url_is_resolved(self):
        url = reverse('users:student_allocation_complete')
        self.assertEquals(resolve(url).func, student_allocation_complete)



    #Manager
    def test_manager_dashboard_url_is_resolved(self):
        url = reverse('users:manager_dashboard')
        self.assertEquals(resolve(url).func, manager_dashboard)

    def test_manager_create_job_url_is_resolved(self):
        url = reverse('users:manager_create_job')
        self.assertEquals(resolve(url).func, manager_create_job)


    




