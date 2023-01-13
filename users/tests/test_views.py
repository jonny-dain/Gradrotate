from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import *
from django.contrib.auth.models import Group
import json

class StudentFormViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.test_group = Group.objects.create(name='Intern')
        self.user.groups.add(self.test_group)
        self.user.save()
        Intern.objects.create(user=self.user)

        Admin.objects.create()
        self.admin = Admin.objects.all().first()
        self.admin.automate_phase = False
        self.admin.phase = 'Intern collection'
        self.admin.save()

        
        self.job_location = JobLocation.objects.create(location = 'office name', address = 'Vodafone, 114, Great Suffolk Street, Bankside, Southwark, London Borough of Southwark, London, Greater London, England, SE1 0BE, United Kingdom', latitude = '51.50117885', longitude = '-0.0998272381710294')

        self.leadership_skills = LeadershipSkills.objects.create(name = 'test')

        self.computing_skills = ComputingSkills.objects.create(name = 'test')
        self.computing_skills2 = ComputingSkills.objects.create(name = 'test2')

        self.analytic_skills = AnalyticSkills.objects.create(name = 'test')
        
        self.marketing_skills = MarketingSkills.objects.create(name = 'test')

        self.management_skills = ManagementSkills.objects.create(name = 'test')

        self.skill1 = ComputingSkills.objects.create(name='Test Skill 1')
        self.skill2 = ComputingSkills.objects.create(name='Test Skill 2')
        self.skill3 = ComputingSkills.objects.create(name='Test Skill 3')
        self.skill4 = AnalyticSkills.objects.create(name='Test Skill 4')
        self.skill5 = MarketingSkills.objects.create(name='Test Skill 5')
        self.skill6 = ComputingSkills.objects.create(name='Test Skill 6')


        self.client.login(username='testuser', password='testpassword')

    #Test student_form
    def test_student_form(self): 
        response = self.client.get(reverse('users:student_form'))
        self.assertEqual(response.status_code, 200)

    def test_student_form_complete_and_saved(self): 
        # test the form submission with correct data
        response = self.client.post(reverse('users:student_form'), {'name': 'Test','email': 'Test@gmail.com'})
        self.assertRedirects(response, reverse('users:student_form_requirements'))
    
        intern = Intern.objects.get(user=self.user)
        self.assertEqual(intern.name, 'Test')

    #Test student_form_requirements
    def test_student_form_requirements(self): 
        response = self.client.get(reverse('users:student_form_requirements'))
        self.assertEqual(response.status_code, 200)

    def test_student_form_requirements_complete_and_saved(self): 
        # test the form submission with correct data
        response = self.client.post(reverse('users:student_form_requirements'), {'remote': '1-2','job_location':self.job_location.pk})
        self.assertRedirects(response, reverse('users:student_form_skills'))

        intern = Intern.objects.get(user=self.user)
        self.assertEqual(intern.remote, '1-2')

    #Test student_form_requirements
    def test_student_form_skills(self): 
        response = self.client.get(reverse('users:student_form_skills'))
        self.assertEqual(response.status_code, 200)

    def test_student_form_skills_empty_form(self): 
        # test the form submission with correct data
        response = self.client.post(reverse('users:student_form_skills'), {'computing_skills': []})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Error completing form')

    def test_student_form_skills_not_submitted(self):

        response = self.client.post(reverse('users:student_form_skills'), {'computing_skills': [self.skill1.pk, self.skill2.pk, self.skill3.pk], 'analytic_skills': [self.skill4.pk], 'marketing_skills': [self.skill5.pk], 'management_skills': [], 'leadership_skills': [], 'business_skills': [], 'admin_skills': []})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Error completing form')
    
    def test_student_form_skills_submitted_and_saved(self):
        response = self.client.post(reverse('users:student_form_skills'), {'computing_skills': [self.skill1.pk, self.skill2.pk, self.skill3.pk], 'analytic_skills': [self.skill4.pk], 'marketing_skills': [self.skill5.pk], 'management_skills': [], 'leadership_skills': [], 'business_skills': [], 'admin_skills': [], 'Submit': 'Submit'})
        self.assertEqual(response.status_code, 302)

        intern = Intern.objects.get(user=self.user)
        computing_skills = intern.computing_skills.all()
        self.assertEqual(len(computing_skills), 3)


    def test_student_allocation_complete_view(self):
        self.admin.phase = 'Allocation'
        self.admin.save()
        response = self.client.get(reverse('users:student_allocation_complete'))
        self.assertEqual(response.status_code, 200)


class ManagerFormViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword', email = "manager@gmail.com")
        self.test_group = Group.objects.create(name='Manager')
        self.user.groups.add(self.test_group)
        self.user.save()
        self.manager = Manager.objects.create(user=self.user)

        Admin.objects.create()
        self.admin = Admin.objects.all().first()
        self.admin.automate_phase = False
        self.admin.phase = 'Job creation'
        self.admin.save()

        
        self.job_location = JobLocation.objects.create(location = 'office name', address = 'Vodafone, 114, Great Suffolk Street, Bankside, Southwark, London Borough of Southwark, London, Greater London, England, SE1 0BE, United Kingdom', latitude = '51.50117885', longitude = '-0.0998272381710294')
        
        self.skill1 = ComputingSkills.objects.create(name='Test Skill 1')
        self.skill2 = ComputingSkills.objects.create(name='Test Skill 2')
        self.skill3 = ComputingSkills.objects.create(name='Test Skill 3')
        self.skill4 = AnalyticSkills.objects.create(name='Test Skill 4')
        self.skill5 = MarketingSkills.objects.create(name='Test Skill 5')
        self.skill6 = ComputingSkills.objects.create(name='Test Skill 6')

        self.client.login(username='testuser', password='testpassword')

    
    def test_manager_dashboard_view(self):
        response = self.client.get(reverse('users:manager_dashboard'))
        self.assertEqual(response.status_code, 200)
    
    def test_manager_create_job_view(self):
        response = self.client.get(reverse('users:manager_create_job'))
        self.assertEqual(response.status_code, 302)

        job = Job.objects.all().first()
        self.assertEqual(job.manager, self.manager)  # check if the manager is correctly associated with the job
        self.assertEqual(job.email, self.user.email)  # check if the email is correctly set

    def test_manager_delete_job_view(self):
        job = Job.objects.create(manager=self.manager)
        response = self.client.get(reverse('users:managerDeleteJob', args=[job.pk]))
        self.assertEqual(response.status_code, 302)

        
    def test_manager_form_view(self):

        job = Job.objects.create(manager=self.manager)
        response = self.client.get(reverse('users:managerForm', args=[job.pk]))
        self.assertEqual(response.status_code, 200)
        
        response = self.client.post(reverse('users:managerForm', args=[job.pk]), {'manager_name': 'manager', 'Submit_form': 'Submit_form'})
        self.assertEqual(response.status_code, 302)

        job = Job.objects.get(manager=self.manager)
        self.assertEqual(job.manager_name, 'manager')

    
    def test_manager_form_requirements_view(self):
        job = Job.objects.create(manager=self.manager)
        response = self.client.get(reverse('users:managerForm2', args=[job.pk]))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('users:managerForm2', args=[job.pk]), {'name': 'job', 'description':'description','daily_tasks': 'daily tasks', 'Submit': 'Submit'})
        self.assertEqual(response.status_code, 302)

        job = Job.objects.get(manager=self.manager)
        self.assertEqual(job.name, 'job')



    def test_manager_form_additional_requirements_view(self):
        job = Job.objects.create(manager=self.manager)
        response = self.client.get(reverse('users:managerForm3', args=[job.pk]))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('users:managerForm3', args=[job.pk]), {'job_location': self.job_location.pk,'wage_value':'25000','team':'team','remote':'Everyday', 'Submit_form': 'Submit_form'})
        self.assertEqual(response.status_code, 302)

        job = Job.objects.get(manager=self.manager)
        self.assertEqual(job.wage, 25000)

        # Could be a section for create a new office locaiton


    def test_manager_form_skills_view(self):
        job = Job.objects.create(manager=self.manager)
        response = self.client.get(reverse('users:managerForm4', args=[job.pk]))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('users:managerForm4', args=[job.pk]), {'computing_skills': [self.skill1.pk, self.skill2.pk, self.skill3.pk], 'analytic_skills': [self.skill4.pk], 'marketing_skills': [self.skill5.pk], 'management_skills': [], 'leadership_skills': [], 'business_skills': [], 'admin_skills': [], 'Submit_form': 'Submit_form'})
        self.assertEqual(response.status_code, 302)

        job = Job.objects.get(manager=self.manager)
        computing_skills = job.computing_skills.all()
        self.assertEqual(len(computing_skills), 3)

    
    def test_manager_form_skills_not_submitted(self): 
        job = Job.objects.create(manager=self.manager)
        response = self.client.post(reverse('users:managerForm4', args=[job.pk]), {'computing_skills': []})
        self.assertEqual(response.status_code, 200)

    def test_manager_form_complete_view(self):
        job = Job.objects.create(manager=self.manager)
        response = self.client.get(reverse('users:managerForm5', args=[job.pk]))
        self.assertEqual(response.status_code, 200)

    
    def test_manager_allocation_complete_view(self):
        self.admin.phase = 'Allocation'
        self.admin.save()
        response = self.client.get(reverse('users:manager_allocation_complete'))
        self.assertEqual(response.status_code, 200)

    





    

 

        
        
    

        