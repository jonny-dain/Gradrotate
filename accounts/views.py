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
            role = form.cleaned_data.get('role_selection')
            group = Group.objects.get(name = role)
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            request.user.groups.add(group)
            #want to redirect user to each place
            return redirect('../dashboard')

    context = {
        'form' : form
    }
    return render(request, 'accounts/register.html', context)

