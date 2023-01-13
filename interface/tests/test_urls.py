from django.test import SimpleTestCase
from django.urls import reverse, resolve
from interface.views import *

class TestUrls(SimpleTestCase):

    def test_admin_interface_url_is_resolved(self):
        url = reverse('admin_interface:admin_interface')
        self.assertEquals(resolve(url).func, admin_interface)

    def test_admin_interface_interns_url_is_resolved(self):
        url = reverse('admin_interface:intern_interface')
        self.assertEquals(resolve(url).func, intern_interface)

    def test_admin_interface_jobs_url_is_resolved(self):
        url = reverse('admin_interface:job_interface')
        self.assertEquals(resolve(url).func, job_interface)

    def test_admin_interface_allocate_excel_url_is_resolved(self):
        url = reverse('admin_interface:allocate_excel')
        self.assertEquals(resolve(url).func, allocate_excel)
    
    def test_admin_interface_allocate_interface_url_is_resolved(self):
        url = reverse('admin_interface:allocate_interface')
        self.assertEquals(resolve(url).func, allocate_interface)
    



    



    

    




