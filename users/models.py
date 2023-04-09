from django.db import models
from accounts.models import Job





#Intern preferences displayed here
class InternPreference(models.Model):

    intern = models.ForeignKey("accounts.Intern", null = True, on_delete = models.SET_NULL)
    job = models.ForeignKey("accounts.Job", null = True, blank = True, on_delete = models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add = True, null = True)


  
    jobs = Job.objects.all()
    

    preference = models.IntegerField(blank=True)

