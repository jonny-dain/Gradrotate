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
            
            intern.progress = 2
            form.save()
            return redirect('../../form/student_form/requirements')


    context = {'form': form, 'intern': intern}
    return render(request, 'users/student_form.html', context)
    

def student_form_requirements(request):
    intern = request.user.intern
    form = StudentForm2(instance= intern)

    if request.method == "POST":
        form = StudentForm2(request.POST, instance= intern) 
        if form.is_valid():
            intern.progress = 2
            intern.location = request.POST['pref_location']
            intern.remote = request.POST['remote_option']
            form.save()
            return redirect('../../form/student_form/skills')

    context = {'form': form, 'intern': intern}
    return render(request, 'users/student_form2.html', context)

def student_form_skills(request):
    intern = request.user.intern
    form = StudentForm3(instance= intern)

    if request.method == "POST":
        form = StudentForm3(request.POST, instance= intern) 
        if form.is_valid():
            intern.progress = 2
            #gathers all the skills
            intern.coding = form.data['coding']
            intern.project_management = form.data['project_management']
            intern.marketing_skills = form.data['marketing_skills']
            intern.web_skills = form.data['web_skills']
            form.save()
            return redirect('../../dashboard')

    context = {'form': form, 'intern': intern}
    return render(request, 'users/student_form3.html', context)



    
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
            form.save()
            job.progress = 2
            return redirect('../../form/manager_form/requirements')


    context = {'form': form, 'job': job}
    return render(request, 'users/manager_form.html', context)

def manager_form_requirements(request):
    job = request.user.job
    #.job
    form = ManagerForm2(instance= job)

    if request.method == 'POST':
        form = ManagerForm2(request.POST, instance= job)        
        if form.is_valid():
            #gathers all the skills
            form.save()
            job.progress = 2
            return redirect('../../form/manager_form/skills')

    context = {'form': form, 'job': job}
    return render(request, 'users/manager_form2.html', context)

    

def manager_form_skills(request):
    job = request.user.job
    #.job
    form = ManagerForm3(instance= job)

    if request.method == 'POST':
        form = ManagerForm3(request.POST, instance= job)        
        if form.is_valid():
            #gathers all the skills
            form.save()
            job.progress = 2
            return HttpResponse("done")

    context = {'form': form, 'job': job}
    return render(request, 'users/manager_form3.html', context)