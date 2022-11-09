from email.policy import HTTP
from unicodedata import name
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.permissions import allowed_users
from .forms import *


# Create your views here.

#@login_required(login_url='../login')
#@allowed_users(allowed_roles=['Intern'])
def student_form(request):
    intern = request.user.intern
    form = StudentForm(instance= intern)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance= intern)        
        if form.is_valid():
            #gathers all the skills
            intern.coding = form.data['coding']
            intern.project_management = form.data['project_management']
            intern.marketing_skills = form.data['marketing_skills']
            intern.web_skills = form.data['web_skills']
            form.save()
            return redirect('../../dashboard')


    context = {'form': form, 'intern': intern}
    return render(request, 'users/student_form.html', context)
    




    
#@login_required(login_url='../login')
#@allowed_users(allowed_roles=['Manager'])
def manager_form(request):
    job = request.user.job
    #.job
    form = ManagerForm(instance= job)

    if request.method == 'POST':
        form = ManagerForm(request.POST, instance= job)        
        if form.is_valid():
            #gathers all the skills
            job.coding = form.data['coding']
            job.project_management = form.data['project_management']
            job.marketing_skills = form.data['marketing_skills']
            job.web_skills = form.data['web_skills']
            form.save()
            return HttpResponse("done")


    context = {'form': form, 'job': job}
    return render(request, 'users/manager_form.html', context)