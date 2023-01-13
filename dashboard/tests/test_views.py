from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import *
from dashboard.views import *

from django.contrib.auth.models import Group


from users.models import InternPreference

class DashboardViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.test_group = Group.objects.create(name='Intern')
        self.user.groups.add(self.test_group)
        self.user.save()
        self.client.login(username='testuser', password='testpassword')
        
        self.intern = Intern.objects.create(user=self.user)

        Admin.objects.create()
        self.admin = Admin.objects.all().first()
        self.admin.automate_phase = False
        self.admin.phase = 'Intern collection'
        self.admin.save()

        

        self.job1 = Job.objects.create(name='Job 1')
        self.job2 = Job.objects.create(name='Job 2')
        self.job3 = Job.objects.create(name='Job 3')


    #Test student_form
    def test_dashboard(self): 
        
        response = self.client.get(reverse('dashboard:preference'))
        self.assertEqual(response.status_code, 200)
       
        self.assertEqual(InternPreference.objects.filter(intern=self.intern).count(), 3)
        self.assertTrue(InternPreference.objects.filter(intern=self.intern, job=self.job1).exists())
        self.assertTrue(InternPreference.objects.filter(intern=self.intern, job=self.job2).exists())
        self.assertTrue(InternPreference.objects.filter(intern=self.intern, job=self.job3).exists())
    
    def test_preference_sets_correct_preference_values(self):
        # create an intern for the user
        

        # make a request to the preference view
        response = self.client.get(reverse('dashboard:preference'))

        # check that the preference values are set correctly
        self.assertEqual(InternPreference.objects.get(intern=self.intern, job=self.job1).preference, 1)
        self.assertEqual(InternPreference.objects.get(intern=self.intern, job=self.job2).preference, 2)
        self.assertEqual(InternPreference.objects.get(intern=self.intern, job=self.job3).preference, 3)

   


    


        