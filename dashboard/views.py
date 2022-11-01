from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.models import Job

# Create your views here.

#@login_required(login_url='../login')
#@allowed_users(allowed_roles=['Intern'])
def preference(request):

    jobs = Job.objects.all()
    jobs_count = jobs.count()
    context = {'jobs' :jobs, 'jobs_count': range(jobs_count)}
    return render(request, 'dashboard/dashboard.html', context)
    