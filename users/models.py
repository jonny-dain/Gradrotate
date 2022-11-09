from django.db import models



# Create your models here. from accounts.models import Intern, Job

class Skills(models.Model):
    name = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return self.name

#Intern preferences displayed here
class InternPreference(models.Model):

    intern = models.ForeignKey("accounts.Intern", null = True, on_delete = models.SET_NULL)
    job = models.ForeignKey("accounts.Job", null = True, blank = True, on_delete = models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add = True, null = True)

    #Preference number for each of the jobs - Needs to be a max number of job.number Job.objects.all() job.count()
    #first preference .. second preference
    #(default=10, validators=[MinValueValidator(1), MaxValueValidator(100)])
  
    preference = models.PositiveSmallIntegerField(default = 0)







#class JobPreference