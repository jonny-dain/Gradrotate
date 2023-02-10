from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import *
from django.contrib.auth.models import Group
import json
import datetime

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.register_url = reverse('register')
        self.logout_url = reverse('logout')

        Admin.objects.create()
        self.admin = Admin.objects.all().first()
        self.admin.automate_phase = False
        self.admin.save()


    def test_login(self):
        response = self.client.get(self.login_url)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_register(self):
        response = self.client.get(self.register_url)
        self.assertTemplateUsed(response, 'accounts/register.html')


class LoginTest(TestCase):

    def setUp(self):
        self.test_user = User.objects.create_user(username='testuser', password='testpassword')
        self.test_group = Group.objects.create(name='Intern')
        self.test_user.groups.add(self.test_group)
        self.test_user.save()
        Intern.objects.create(user=self.test_user)


        Admin.objects.create()
        self.admin = Admin.objects.all().first()
        self.admin.automate_phase = False
        self.admin.phase = 'Intern collection'
        self.admin.save()

        return super().setUp()

    def test_login(self):
        # make sure the login page can be accessed
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_wrong_login(self):
        # test the login functionality with incorrect credentials
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Username or password is incorrect')
    
    def test_correct_login(self):
        # test the login functionality with correct credentials
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)


class RegisterViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        Admin.objects.create()
        Group.objects.create(name='Intern')
        Group.objects.create(name='Admin')
        Group.objects.create(name='Manager')

    def test_register(self):
        # make sure the register page can be accessed
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_correct_register(self):
        # test the register functionality with correct data
        response = self.client.post(reverse('register'), {'username': 'testuser', 'email': 'test@example.com', 'password1': 'testpassword', 'password2': 'testpassword', 'role_selection': 'Intern'})
        self.assertEqual(response.status_code, 302)
    
        # test that user was created in the database
        self.assertTrue(User.objects.filter(username='testuser').exists())
        self.assertTrue(Intern.objects.filter(user__username='testuser').exists())

        # test that the proper role was assigned to the user
        user = User.objects.get(username='testuser')
        self.assertEqual(user.groups.first().name, 'Intern')
    
    def test_wrong_register(self):
        # test the register functionality with mismatched passwords
        response = self.client.post(reverse('register'), {'username': 'testuser', 'email': 'test@example.com', 'password1': 'testpassword', 'password2': 'wrongpassword', 'role_selection': 'Intern'})
        self.assertEqual(response.status_code, 200)
        
    def test_invalid_email_register(self):
        # test the register functionality with invalid email
        response = self.client.post(reverse('register'), {'username': 'testuser', 'email': 'test.com', 'password1': 'testpassword', 'password2': 'testpassword', 'role_selection': 'Intern'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Enter a valid email address')

class HomepageViewTestCase(TestCase):
    def setUp(self):
        

        Admin.objects.create(
            total_interns=5,
            total_jobs=10
        )
        self.admin = Admin.objects.all().first()
        self.admin.automate_phase = False
        self.admin.phase = 'Intern collection'
        self.admin.save()
    
    def test_homepage_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_homepage_stats(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, '5')

    def test_hompage_stats(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, '10')
    



class LogoutTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.user.save()

        Admin.objects.create()
        self.admin = Admin.objects.all().first()
        self.admin.automate_phase = False
        self.admin.phase = 'Intern collection'
        self.admin.save()
        
    def test_logout(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('home'))
        self.assertEqual(str(response.status_code), '302')
        self.assertNotIn('_auth_user_id', self.client.session)