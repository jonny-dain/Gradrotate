from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.permissions import allowed_users

# Create your views here.

#@login_required(login_url='../login')
#@allowed_users(allowed_roles=['Intern'])
def student_form(request):
    #name = request.user.Interns.name()

    return render(request, 'users/student_form.html')
    
#@login_required(login_url='../login')
#@allowed_users(allowed_roles=['Manager'])
def manager_form(request):
    return render(request, 'users/manager_form.html')