import email
from sre_constants import CATEGORY
from django.db import models
from users.models import Skills
from django.contrib.auth.models import User


# Create your models here.  I want to create a customer user for email authenication I think... https://www.youtube.com/watch?v=vGDNJoeeQaA




class Intern(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length = 200, null = True)
    #email = User.email
    email = models.CharField(max_length = 200, null = True)
    date_created = models.DateTimeField(auto_now_add=True)
    skills = models.ManyToManyField(Skills)

    #Skills
    coding = models.IntegerField(default = 5)
    project_management = models.IntegerField(default = 5)
    marketing_skills = models.IntegerField(default = 5)
    web_skills = models.IntegerField(default = 5)

    


    def __str__(self):
        return str(self.name)


class Job(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    JOB_LOCATIONS = (
        ('Newbury','Newbury'),
        ('London Paddington', 'London Paddington'),
        ('Speechmark','Speechmark'),
    )
    
    name = models.CharField(max_length = 200, null = True)
    location = models.CharField(max_length = 200, null = True, choices = JOB_LOCATIONS)
    description = models.CharField(max_length = 200, null = True, blank = True)
    date_created = models.DateTimeField(auto_now_add=True)
    skills = models.ManyToManyField(Skills)

    #Skills
    coding = models.IntegerField(default = 5)
    project_management = models.IntegerField(default = 5)
    marketing_skills = models.IntegerField(default = 5)
    web_skills = models.IntegerField(default = 5)

    def __str__(self):
        return str(self.name)


