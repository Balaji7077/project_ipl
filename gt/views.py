from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def pandya(request):
    return render(request,'pandya.html')
def gill(request):
    return HttpResponse('<h1> bhabi hoto kaisi ho sar bhabi jasi ho </h1>')