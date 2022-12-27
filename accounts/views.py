from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .permissions import authenticated_user, allowed_users, update_phase
from django.contrib.auth.models import Group


# Create your views here.
from .models import *
from .forms import CreateUserForm

#Testing
import datetime


@update_phase
@authenticated_user
def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        admin = Admin.objects.all().first()

        if user is not None:
            auth_login(request, user)

            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

                if group == 'Admin':
                    return redirect('../../admin_interface')
                
                if (admin.phase == 'Job creation'):
                    if group == 'Manager':
                        return redirect('../form/manager_form')
                    else:
                        auth_logout(request)
                if (admin.phase == 'Intern collection'):
                    if group == 'Intern':
                        return redirect('../form/student_form')
                    else:
                        auth_logout(request)
                messages.info(request, 'We are currently in the '+ str(admin.phase)+ ' phase, please try again later')

                return render(request, 'accounts/login.html')

        else:
            messages.info(request, 'Username or password is incorrect')
            return render(request, 'accounts/login.html')


    return render(request, 'accounts/login.html')

def logout(request):  
    auth_logout(request)
    return redirect('../login')
    
      
@authenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            role = request.POST['role_selection']
            username = request.POST['username'] 
            user = form.save()
            group = Group.objects.get(name = role)
            user.groups.add(group)
            if role == 'Admin':
                return redirect('../../interface')
            if role == 'Manager':
                Job.objects.create(
                    user = user,
                    email = user.email,
                    
                )
            if role == 'Intern':
                Intern.objects.create(
                    user = user,
                    email = user.email,
                )
            
            messages.success(request, 'Account was greated for '+ str(username) )
            return redirect('../login')

    context = {
        'form' : form
    }
    return render(request, 'accounts/register.html', context)

