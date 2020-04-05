from django.shortcuts import render
from django.http import HttpResponse 

def index(request):
    return HttpResponse("Django Demo Application.") 
 #Create your views here.
def greeting(request):
     return HttpResponse("Hello fool.")
