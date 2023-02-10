from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import *
from django.contrib.auth.models import Group
import json
import datetime

class UpdatePhaseDecoratorTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='secret'
        )
        self.admin = Admin.objects.create(
            automate_phase=True,
            allocation_creation_date=datetime.date(2022, 1, 1),
            intern_creation_date=datetime.date(2022, 2, 1),
        )
        self.admin.phase = 'Job creation'

    def test_update_phase_decorator(self):
        response = self.client.get(reverse('home'))
        self.admin.refresh_from_db()
        
        self.assertEqual(self.admin.phase, 'Allocation')

    def test_update_phase_decorator_2(self):
        with self.settings(NOW=datetime.datetime(2022, 1, 2)):
            response = self.client.get(reverse('home'))
        self.admin.refresh_from_db()
        self.assertEqual(self.admin.phase, 'Allocation')

    def test_update_phase_decorator_3(self):
        with self.settings(NOW=datetime.datetime(2022, 2, 2)):
            response = self.client.get(reverse('home'))
        self.admin.refresh_from_db()
        self.assertEqual(self.admin.phase, 'Allocation')


class UpdateProgressDecoratorTests(TestCase):
    def setUp(self):
        self.group = Group.objects.create(name='Intern')
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='secret'
        )
        self.user.groups.add(self.group)
        self.intern = Intern.objects.create(
            user=self.user,
            progress=0
        )
        self.admin = Admin.objects.create(
            automate_phase=True,
            allocation_creation_date=datetime.date(2022, 1, 1),
            intern_creation_date=datetime.date(2022, 2, 1),
        )
        self.admin.phase = 'Intern collection'

    def test_update_progress_decorator(self):
        # Ensure the progress is 0 before the request
        self.intern.refresh_from_db()
        self.assertEqual(self.intern.progress, 0)


class AllowedUsersDecoratorTests(TestCase):
    def setUp(self):
        self.admin_group = Group.objects.create(name='Admin')
        self.manager_group = Group.objects.create(name='Manager')
        self.intern_group = Group.objects.create(name='Intern')
        self.admin = User.objects.create_user(
            username='admin',
            email='admin@example.com',
            password='secret'
        )
        self.admin.groups.add(self.admin_group)
        self.manager = User.objects.create_user(
            username='manager',
            email='manager@example.com',
            password='secret'
        )
        self.manager.groups.add(self.manager_group)
        self.intern = User.objects.create_user(
            username='intern',
            email='intern@example.com',
            password='secret'
        )
        self.intern.groups.add(self.intern_group)

        self.admin = Admin.objects.create(
            automate_phase=True,
            allocation_creation_date=datetime.date(2022, 1, 1),
            intern_creation_date=datetime.date(2022, 2, 1),
        )
        self.admin.phase = 'Intern collection'
        self.admin.save()

    def test_allowed_users_decorator(self):

        self.client.login(username='admin', password='secret')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.client.login(username='manager', password='secret')

        response = self.client.get(reverse('home'))

       
        self.assertEqual(response.status_code, 200)
        

        self.client.login(username='intern', password='secret')

        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        

