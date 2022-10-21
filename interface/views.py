from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def admin_interface(request):
    return render(request, 'interface/interface.html')