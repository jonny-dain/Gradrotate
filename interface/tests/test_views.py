from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from accounts.models import *
from interface.views import *

from django.contrib.auth.models import Group


from users.models import InternPreference

from django.conf import settings
from pathlib import Path

class AdminViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.test_group = Group.objects.create(name='Admin')
        self.user.groups.add(self.test_group)
        self.user.save()
        self.client.login(username='testuser', password='testpassword')
        
        self.user2=User.objects.create_user(username='testuser2', password='testpassword2')
        self.test_group2 = Group.objects.create(name='Intern')
        self.user2.groups.add(self.test_group2)
        self.user2.save()
        self.intern = Intern.objects.create(user=self.user2)

        self.user3=User.objects.create_user(username='testuser3', password='testpassword3')
        self.manager = Manager.objects.create(user=self.user3)

        Admin.objects.create(user= self.user)
        self.admin = Admin.objects.all().first()
        self.admin.automate_phase = False
        self.admin.phase = 'Intern collection'
        self.admin.save()

        self.job_location = JobLocation.objects.create(location = 'office name', address = 'Vodafone, 114, Great Suffolk Street, Bankside, Southwark, London Borough of Southwark, London, Greater London, England, SE1 0BE, United Kingdom', latitude = '51.50117885', longitude = '-0.0998272381710294')

        self.leadership_skills = LeadershipSkills.objects.create(name = 'test')
        self.computing_skills = ComputingSkills.objects.create(name = 'test')
        self.analytic_skills = AnalyticSkills.objects.create(name = 'test')
        self.marketing_skills = MarketingSkills.objects.create(name = 'test')
        self.management_skills = ManagementSkills.objects.create(name = 'test')
        self.business_skills = BusinessSkills.objects.create(name = 'test')
        self.admin_skills = AdminSkills.objects.create(name = 'test')

        self.factory = RequestFactory()
        self.job = Job.objects.create(name='test_job', manager=self.manager)
        self.intern_preference = InternPreference.objects.create(job=self.job, intern = self.intern, preference= '2')
    
   
     


    def test_allocate_interface_view(self): 
        response = self.client.get(reverse('interface:allocate_interface'))
        self.assertEqual(response.status_code, 302)

    def test_delete_job_view(self):
        request = self.factory.get(reverse('interface:deleteJob', kwargs={'pk': self.job.pk}))

        request.user = self.user
        response = deleteJob(request, pk=self.job.pk)
        self.assertEqual(response.status_code, 302)

        self.assertFalse(Job.objects.filter(id=self.job.pk).exists())
        self.assertFalse(InternPreference.objects.filter(job=self.job).exists())

    def test_delete_intern_view(self):
        request = self.factory.get(reverse('interface:deleteIntern', kwargs={'pk': self.intern.pk}))
        request.user = self.user
        response = deleteIntern(request, pk=self.intern.pk)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Intern.objects.filter(id=self.intern.pk).exists())
        self.assertFalse(InternPreference.objects.filter(intern=self.intern).exists())

    def test_delete_office_view(self):
        request = self.factory.get(reverse('interface:deleteOffice', kwargs={'pk': self.job_location.pk}))
        request.user = self.user
        response = deleteOffice(request, pk=self.job_location.pk)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(JobLocation.objects.filter(id=self.job_location.pk).exists())
        
    def test_delete_skill_computing(self):
        request = self.factory.get(reverse('interface:deleteSkillComputing', kwargs={'pk': self.computing_skills.pk}))
        request.user = self.user
        response = deleteSkillComputing(request, pk=self.computing_skills.pk)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(ComputingSkills.objects.filter(id=self.computing_skills.pk).exists())

    def test_delete_skill_leadership(self):
        request = self.factory.get(reverse('interface:deleteSkillLeadership', kwargs={'pk': self.leadership_skills.pk}))
        request.user = self.user
        response = deleteSkillLeadership(request, pk=self.leadership_skills.pk)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(LeadershipSkills.objects.filter(id=self.leadership_skills.pk).exists())

    def test_delete_skill_computing(self):
        request = self.factory.get(reverse('interface:deleteSkillComputing', kwargs={'pk': self.computing_skills.pk}))
        request.user = self.user
        response = deleteSkillComputing(request, pk=self.computing_skills.pk)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(ComputingSkills.objects.filter(id=self.computing_skills.pk).exists())

    def test_delete_skill_analytic(self):
        request = self.factory.get(reverse('interface:deleteSkillAnalytic', kwargs={'pk': self.analytic_skills.pk}))
        request.user = self.user
        response = deleteSkillAnalytic(request, pk=self.analytic_skills.pk)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(AnalyticSkills.objects.filter(id=self.analytic_skills.pk).exists())

    def test_delete_skill_marketing(self):
        request = self.factory.get(reverse('interface:deleteSkillMarketing', kwargs={'pk': self.marketing_skills.pk}))
        request.user = self.user
        response = deleteSkillMarketing(request, pk=self.marketing_skills.pk)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(MarketingSkills.objects.filter(id=self.marketing_skills.pk).exists())

    def test_delete_skill_management(self):
        request = self.factory.get(reverse('interface:deleteSkillManagement', kwargs={'pk': self.management_skills.pk}))
        request.user = self.user
        response = deleteSkillManagement(request, pk=self.management_skills.pk)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(ManagementSkills.objects.filter(id=self.management_skills.pk).exists())
    
    def test_delete_skill_business(self):
        request = self.factory.get(reverse('interface:deleteSkillBusiness', kwargs={'pk': self.business_skills.pk}))
        request.user = self.user
        response = deleteSkillBusiness(request, pk=self.business_skills.pk)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(BusinessSkills.objects.filter(id=self.business_skills.pk).exists())


class AdminViewTestExcel(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.test_group = Group.objects.create(name='Admin')
        self.user.groups.add(self.test_group)
        self.user.save()
        self.client.login(username='testuser', password='testpassword')

        Admin.objects.create(user= self.user)
        self.admin = Admin.objects.all().first()
        self.admin.automate_phase = False
        self.admin.phase = 'Intern collection'
        self.admin.save()
    

    def test_allocate_excel(self):
        response = self.client.get(reverse('interface:allocate_excel'))
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'interface/allocate_excel.html')

    def test_post_request_with_valid_excel_file(self):
        
        path = Path(settings.BASE_DIR).joinpath("static", "files", "Placement_test.xlsx")
        excel_file = open(path, "rb")       
        response = self.client.post(reverse('interface:allocate_excel'), {'excel_file': excel_file})
        self.assertEqual(response.status_code, 302)
        
    





       



    











    