from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .permissions import authenticated_user, allowed_users
from django.contrib.auth.models import Group


# Create your views here.
from .models import *
from .forms import CreateUserForm


@authenticated_user
def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            auth_login(request, user)

            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

                if group == 'Admin':
                    return redirect('../../admin_interface')
                
                if group == 'Manager':
                    return redirect('../form/manager_form')
                
                if group == 'Intern':
                    return redirect('../form/student_form')
                else:
                    return HttpResponse('You are not authorized to view this page')
            
            return redirect('../dashboard')

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
            #role = request.POST['role_selection']
            username = request.POST['username'] 
            user = form.save()
            #group = Group.objects.get(name = role)
            #user.groups.add(group)
            #if role == 'Admin':
            #    return redirect('../../interface')
            #if role == 'Manager':
            #    Job.objects.create(
            #        user = user,
            #        manager_name=user.username,
            #        email = user.email,
            #        
            #    )
            #if role == 'Intern':
            #    Intern.objects.create(
            #        user = user,
            #        name= user.username,
            #        email = user.email,
            #    )
            
            messages.success(request, 'Account was greated for '+ str(username) )
            return redirect('../login')

    context = {
        'form' : form
    }
    return render(request, 'accounts/register.html', context)

