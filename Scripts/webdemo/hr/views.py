from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
import requests
import json
import sys

def welcome(request):
    return HttpResponse("<h1> Welcome to HR</h1>")
# Create your views here
def index(request):
    #return HttpResponse("Index page")
    return render(request,'index.html')
def list_employees(request):
    con=sqlite3.connect(r"/home/gundapu/Python/sqlite-tools-linux-x86-3310100/hr.db")
    cur=con.cursor()
    cur.execute("select * from employees")
    emps=cur.fetchall()
    con.close()
    return render(request,'list_employees.html',{"employees":emps})

def countriesnandp(request):
    resp=requests.get('https://restcountries.eu/rest/v2/all')
    if resp.status_code != 200:
        print("sorry")
        sys.exit(1)
    else:
        details=resp.json()
        return render(request,'countries.html',{"cname":details})
#return render(request,'countries.html', {"Countries":details})
        
