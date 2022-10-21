from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def student_form(request):
    return render(request, 'users/student_form.html')
    

def manager_form(request):
    return render(request, 'users/manager_form.html')