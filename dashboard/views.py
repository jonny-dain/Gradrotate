from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def preference(request):
    return HttpResponse("this is the student preference page")