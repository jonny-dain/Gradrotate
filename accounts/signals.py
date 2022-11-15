from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import *

def intern_profile(sender, instance, created, **kwargs):
    if created:
            group = Group.objects.get(name = 'Intern')
            instance.groups.add(group)
            Intern.objects.create(
                    user = instance,
                    name= instance.username,
                    email = instance.email,
                )
            print('profile created! ')

post_save.connect(intern_profile, sender = User)