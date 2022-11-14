from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.models import *
from interface.preferences import *
from users.models import *

# Create your views here.

#@login_required(login_url='../login')
#@allowed_users(allowed_roles=['Admin'])
def admin_interface(request):
    
    jobs = Job.objects.all()
    interns = Intern.objects.all()

    #intern_preference_dictionary()



    context = {'jobs' :jobs , 'interns' : interns}
    return render(request, 'interface/interface.html', context)

#This is to delete Interns from the system
#@login_required(login_url='../login')
#@allowed_users(allowed_roles=['Admin'])
def deleteIntern(request, pk):

    interns = Intern.objects.all()
    intern = Intern.objects.get(id=pk)
    InternPreference.objects.filter(intern = intern).delete()
    User.objects.get(intern = intern).delete()
    intern.delete()
    #need to delete all interns items
    return redirect('../../../admin_interface/')

