from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import *

class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)