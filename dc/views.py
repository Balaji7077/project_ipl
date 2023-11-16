from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def pant(request):
    return render(request,'pant.html')

def warner(request):
    return HttpResponse('<h1> warner jhukaga nahi sala </h1>')