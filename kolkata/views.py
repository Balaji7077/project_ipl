from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def iyer(request):
    return render(request,'iyer.html')
def rinku(request):
    return HttpResponse('<h1> king of kolkata </h1>')