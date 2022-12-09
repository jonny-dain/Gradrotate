from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Intern)
admin.site.register(Job)
admin.site.register(Admin)
admin.site.register(ComputingSkills)
admin.site.register(AnalyticSkills)
admin.site.register(MarketingSkills)
admin.site.register(ManagementSkills)
admin.site.register(LeadershipSkills)
admin.site.register(BusinessSkills)
admin.site.register(AdminSkills)
admin.site.register(JobLocation)

