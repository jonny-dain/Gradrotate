from django.test import SimpleTestCase
from django.urls import reverse, resolve
from dashboard.views import *

class TestUrls(SimpleTestCase):

    def test_dashboard_url_is_resolved(self):
        url = reverse('dashboard:preference')
        self.assertEquals(resolve(url).func, preference)

    def test_sort_url_is_resolved(self):
        url = reverse('dashboard:sort')
        self.assertEquals(resolve(url).func, sort)






