from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Djange Demo Application")

def hello(request):
    if 'name' in request.GET:
        name=request.GET['name']
    else:
        name="Guest"
    return HttpResponse("<h1>Welcome "+name+"</h1>")      
