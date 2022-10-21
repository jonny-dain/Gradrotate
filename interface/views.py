from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def admin_interface(request):
    return HttpResponse("this is the admin interface")