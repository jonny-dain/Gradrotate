from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .permissions import allowed_users, update_phase
from django.contrib.auth.models import Group


# Create your views here.
from .models import *
from .forms import CreateUserForm



#Testing
import datetime

#Homepage
@update_phase
def homepage(request):
    admin = Admin.objects.all().first()
    total_interns = admin.total_interns
    total_jobs = admin.total_jobs

    setup_initial_data()

    context = {'total_interns': total_interns, 'total_jobs': total_jobs}
    return render(request, 'accounts/homepage.html', context)




#Login method
@update_phase
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
                        return redirect('../form/manager_dashboard')
                    else:
                        auth_logout(request)
                if (admin.phase == 'Intern collection'):
                    if group == 'Intern':
                        if request.user.intern.progress == 5:
                            return redirect('../form/student_form/complete')
                        return redirect('../form/student_form')
                    else:
                        auth_logout(request)             
                if (admin.phase == 'Allocation'):
                    if group == 'Intern':          
                        return redirect('../../../../form/student_form/allocation/complete')
                    if group == 'Manager':
                        return redirect('../../../../form/manager_form/allocation/complete')        
                messages.info(request, 'We are currently in the '+ str(admin.phase)+ ' phase, please try again later')
                auth_logout(request)
                return render(request, 'accounts/login.html')
        else:
            messages.info(request, 'Username or password is incorrect')
            return render(request, 'accounts/login.html')

    return render(request, 'accounts/login.html')

def logout(request):  
    auth_logout(request)
    return redirect('../')
    
      
# Register system
def register(request):
    admin = Admin.objects.all().first()
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
                Manager.objects.create(
                    user= user,       
                )
            if role == 'Intern':
                Intern.objects.create(
                    user = user,
                    email = user.email,
                )
                admin.total_interns += 1
                admin.save() 
            messages.success(request, 'Account was greated for '+ str(username) )
            return redirect('../login')

    context = {
        'form' : form
    }
    return render(request, 'accounts/register.html', context)




GROUP_NAMES = ['Admin', 'Manager', 'Intern']

# Runs to get up the local host
def setup_initial_data():
    
    # Create user groups
    for group_name in GROUP_NAMES:
        Group.objects.get_or_create(name=group_name)
        
    # Check if there are any admin users already, and create one if not
    admins = Admin.objects.all()
    
    if not admins.exists():
        admin_user = User.objects.create_user(
            username='admin',
            password='supersecretpassword',
        )
        admin_group = Group.objects.get(name='Admin')
        admin_user.groups.add(admin_group)
        admin_user.save()
        admin_object = Admin.objects.create(user=admin_user)


# HTTP Error 400
def bad_request(request, exception):
    return render(request, "accounts/error.html")

# HTTP Error 500
def bad_request_500(request):
    return render(request, "accounts/error.html")
