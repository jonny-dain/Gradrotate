from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import *
from django.contrib.auth.models import Group
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.register_url = reverse('register')
        self.logout_url = reverse('logout')

        




    def test_login(self):
        response = self.client.get(self.login_url)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_register(self):
        response = self.client.get(self.register_url)
        self.assertTemplateUsed(response, 'accounts/register.html')


class LoginTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.register_url = reverse('register')
        self.logout_url = reverse('logout')

        self.user = {
            'username' : 'testintern',
            'email' : 'testintern@gmail.com',
            'password' : 'testpassword'
        }
        self.user2={
            'email':'testemail@gmail.com',
            'username':'username',
            'password':'password',
            'password2':'password',
            'name':'fullname'
        }



        return super().setUp()

    def test_can_register_user(self):
        response=self.client.post(self.register_url,self.user2,format='text/html')
        self.assertEqual(response.status_code,302)


    def test_login_view(self):
        response = self.client.get(self.login_url)

        self.assertEqual(response.status_code, 200)


    def test_login_success(self):



        

        self.client.post(self.register_url,self.user, format ='text/html')
        User.objects.create(
            email = 'testintern@gmail.com',
            username = 'testintern',
            password = 'testpassword',
        )

        user = User.objects.filter(email = self.user['email']).first()
        
       
        if user is not None:
            user.is_active = True
            group = Group.objects.get_or_create(name = 'intern')
            user.groups.add(group)
            
            group = user.groups.all()[0].name
            print(user.group)
            user.save()

        response = self.client.get(self.login_url)

        #response = self.client.post(self.login_url,self.user, format ='text/html')
        print(response)

        #self.assertEqual(response.status_code,302)

        self.client.login(username='testintern', password='testpassword')

        self.assertTrue(response.context['user'].is_authenticated)