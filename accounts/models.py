import email
from sre_constants import CATEGORY
from django.db import models
#from users.models import Skills
from django.contrib.auth.models import User
from django import forms


# Create your models here.  I want to create a customer user for email authenication I think... https://www.youtube.com/watch?v=vGDNJoeeQaA


# Skill category 
class ComputingSkills(models.Model):
    name = models.CharField(max_length = 200, null = True)
    def __str__(self):
        return self.name

class AnalyticSkills(models.Model):
    name = models.CharField(max_length = 200, null = True)
    def __str__(self):
        return self.name

class MarketingSkills(models.Model):
    name = models.CharField(max_length = 200, null = True)
    def __str__(self):
        return self.name

class ManagementSkills(models.Model):
    name = models.CharField(max_length = 200, null = True)
    def __str__(self):
        return self.name

class LeadershipSkills(models.Model):
    name = models.CharField(max_length = 200, null = True)
    def __str__(self):
        return self.name

class BusinessSkills(models.Model):
    name = models.CharField(max_length = 200, null = True)
    def __str__(self):
        return self.name

class AdminSkills(models.Model):
    name = models.CharField(max_length = 200, null = True)
    def __str__(self):
        return self.name




















class Intern(models.Model):

    JOB_LOCATIONS = (
        ('Newbury','Newbury'),
        ('London Paddington', 'London Paddington'),
        ('Speechmark','Speechmark'),
    )
    REMOTE_CHOICES = (
        ('Everyday', 'Everyday'),
        ('3-4', '3-4'),
        ('1-2','1-2'),
        ('Remote','Remote'),
    )

    #Personal information
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length = 200, null = True)
    email = models.CharField(max_length = 200, null = True)
    date_created = models.DateTimeField(auto_now_add=True)

    #not sure I want skills
    computing_skills = models.ManyToManyField(ComputingSkills)
    analytic_skills = models.ManyToManyField(AnalyticSkills)
    marketing_skills = models.ManyToManyField(MarketingSkills)
    management_skills = models.ManyToManyField(ManagementSkills)
    leadership_skills = models.ManyToManyField(LeadershipSkills)
    business_skills = models.ManyToManyField(BusinessSkills)
    admin_skills = models.ManyToManyField(AdminSkills)











    #Job preferences
    location = models.CharField(max_length = 200, null = True, choices = JOB_LOCATIONS)
    remote = models.CharField(max_length = 200, null = True, choices = REMOTE_CHOICES)
    
    #Expected wage
    wage = models.IntegerField(default = 0)


    
    #user progress
    progress = models.IntegerField(default=1)

    #Skills
    #coding = models.IntegerField(default = 5)
    #project_management = models.IntegerField(default = 5)
    #marketing1_skills = models.IntegerField(default = 5)
    #web_skills = models.IntegerField(default = 5)

    def __str__(self):
        return str(self.name)









class Job(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    JOB_LOCATIONS = (
        ('Newbury','Newbury'),
        ('London Paddington', 'London Paddington'),
        ('Speechmark','Speechmark'),
    )

    REMOTE_CHOICES = (
        ('Everyday', 'Everyday'),
        ('3-4', '3-4'),
        ('1-2','1-2'),
        ('Remote','Remote'),
    )


    email = models.CharField(max_length = 200, null = True)
    manager_name = models.CharField(max_length = 200, null = True)
    name = models.CharField(max_length = 200, null = True)

    description = models.CharField(max_length = 200, null = True, blank = True)
    daily_tasks = models.CharField(max_length = 200, null = True, blank = True)




    date_created = models.DateTimeField(auto_now_add=True)

    #Location and remote balance
    location = models.CharField(max_length = 200, null = True, choices = JOB_LOCATIONS)
    remote = models.CharField(max_length = 200, null = True, choices = REMOTE_CHOICES)

    #Wage
    wage = models.IntegerField(default = 0)



    #Skills
    computing_skills = models.ManyToManyField(ComputingSkills)
    analytic_skills = models.ManyToManyField(AnalyticSkills)
    marketing_skills = models.ManyToManyField(MarketingSkills)
    management_skills = models.ManyToManyField(ManagementSkills)
    leadership_skills = models.ManyToManyField(LeadershipSkills)
    business_skills = models.ManyToManyField(BusinessSkills)
    admin_skills = models.ManyToManyField(AdminSkills)


    #user progress
    progress = models.IntegerField(default=1)
    
    #Skills
    #coding = models.IntegerField(default = 5)
    #project_management = models.IntegerField(default = 5)
    #marketing1_skills = models.IntegerField(default = 5)
    #web_skills = models.IntegerField(default = 5)

    def __str__(self):
        return str(self.name)




class Admin(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    PHASES = (
        ('Job creation','Job creation'),
        ('Intern collection','Intern collection'),
        ('Allocation','Allocation'),
    )

    phase = models.CharField(max_length = 200, null = True, choices = PHASES)
    name = models.CharField(max_length = 200, null = True)
    def __str__(self):
        return str(self.name)




