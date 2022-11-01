from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.models import *

# Create your views here.

#@login_required(login_url='../login')
#@allowed_users(allowed_roles=['Admin'])
def admin_interface(request):
    
    jobs = Job.objects.all()
    interns = Intern.objects.all()

    context = {'jobs' :jobs , 'interns' : interns}
    return render(request, 'interface/interface.html')