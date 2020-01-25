from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'my_app/index.html')

def login_functionality(request):
    return HttpResponse('<h1>This is git functionality </h1>')