from django.db import models

# Create your models here.

class Skills(models.Model):
    name = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return self.name



#Intern preferences displayed here
class InternPreference(models.Model):

    date_created = models.DateTimeField(auto_now_add = True, null = True)
    preference = models.IntegerField(default = 1)


#class JobPreference