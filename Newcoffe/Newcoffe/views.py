

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def firstone(request):
    return render(request,'coffeapp/first.html')

def view_emp(request):
    return render(request, 'coffeapp/view.html')
