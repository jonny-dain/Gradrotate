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


class JobLocation(models.Model):
    location = models.CharField(max_length = 200, null = True)
    address = models.TextField() 
    latitude = models.FloatField() 
    longitude = models.FloatField() 
    
    def __str__(self):
        return self.location






    






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
    computing_skills = models.ManyToManyField(ComputingSkills, blank=True)
    analytic_skills = models.ManyToManyField(AnalyticSkills, blank=True)
    marketing_skills = models.ManyToManyField(MarketingSkills, blank=True)
    management_skills = models.ManyToManyField(ManagementSkills, blank=True)
    leadership_skills = models.ManyToManyField(LeadershipSkills, blank=True)
    business_skills = models.ManyToManyField(BusinessSkills, blank=True)
    admin_skills = models.ManyToManyField(AdminSkills, blank=True)

    
    job_location = models.ForeignKey(JobLocation, null=True, on_delete=models.SET_NULL)
    


    remote = models.CharField(max_length = 200, null = True, choices = REMOTE_CHOICES)
    
    


    
    #user progress
    progress = models.IntegerField(default=1)

    #Skills
    #coding = models.IntegerField(default = 5)
    #project_management = models.IntegerField(default = 5)
    #marketing1_skills = models.IntegerField(default = 5)
    #web_skills = models.IntegerField(default = 5)

    allocated_job = models.ForeignKey('Job', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.name)



class Manager(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    

    def __str__(self):
        return str(self.manager_name)  





class Job(models.Model):
    #user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
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


    manager = models.ForeignKey(Manager, null=True, on_delete=models.CASCADE)




    email = models.CharField(max_length = 200, null = True)
    manager_name = models.CharField(max_length = 200, null = True)
    name = models.CharField(max_length = 200, null = True)

    description = models.TextField(null = True, blank = True)
    daily_tasks = models.TextField(null = True, blank = True)



    team = models.CharField(max_length=30, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    #Location and remote balance
    #location = models.CharField(max_length = 200, null = True, choices = JOB_LOCATIONS)

    job_location = models.ForeignKey(JobLocation, null=True, on_delete=models.SET_NULL)

    remote = models.CharField(max_length = 200, null = True, choices = REMOTE_CHOICES)

    #Wage
    wage = models.IntegerField(default = 15000)

    

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

    allocated_intern = models.ForeignKey(Intern, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.name)




class Admin(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    PHASES = (
        ('Job creation','Job creation'),
        ('Intern collection','Intern collection'),
        ('Allocation','Allocation'),
    )
    ALGORITHM =(
        ('Gale Shapely','Gale Shapely'),
        ('Hungarian','Hungarian'),
        ('Pareto','Pareto')

    )

    phase = models.CharField(max_length = 200, null = True, choices = PHASES)

    #automate true or false...
    automate_phase = models.BooleanField(default=False)

    job_creation_date = models.DateField(null=True)
    intern_creation_date  = models.DateField(null=True)
    allocation_creation_date = models.DateField(null=True)

    total_jobs = models.IntegerField(default=0)
    total_interns = models.IntegerField(default=0)

    notify_allocations = models.BooleanField(default=False)
    allocation_algorithm = models.CharField(max_length = 200, null = True, choices = ALGORITHM)

    name = models.CharField(max_length = 200, null = True)
    def __str__(self):
        return str(self.name)




