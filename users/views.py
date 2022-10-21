from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def student_form(request):
    return HttpResponse("this is the student form")


def manager_form(request):
    return HttpResponse("this is the manager form")