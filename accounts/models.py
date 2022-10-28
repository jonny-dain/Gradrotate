import email
from sre_constants import CATEGORY
from django.db import models
from users.models import Skills
from django.contrib.auth.models import User

# Create your models here.

class Intern(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length = 200, null = True)
    email = models.CharField(max_length = 200, null = True)
    date_created = models.DateTimeField(auto_now_add=True)
    skills = models.ManyToManyField(Skills)

    def __str__(self):
        return str(self.name)

class Job(models.Model):
    JOB_LOCATIONS = (
        ('Newbury','Newbury'),
        ('London Paddington', 'London Paddington'),
        ('Speechmark','Speechmark'),
    )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length = 200, null = True)
    location = models.CharField(max_length = 200, null = True, choices = JOB_LOCATIONS)
    description = models.CharField(max_length = 200, null = True, blank = True)
    date_created = models.DateTimeField(auto_now_add=True)
    skills = models.ManyToManyField(Skills)

    def __str__(self):
        return str(self.name)