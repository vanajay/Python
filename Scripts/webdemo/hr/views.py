from django.shortcuts import render,redirect
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
    total=0
    resp=requests.get('https://restcountries.eu/rest/v2/all')
    if resp.status_code != 200:
        print("sorry")
        sys.exit(1)
    else:
        details=resp.json()
        print("hai")
        print(details[0])
        return render(request,'countries.html',{"cname":details,"totalpop":total})
       

#def add_employee(request):
    #if 'fullname' in request.GET:
#        print("hello")
#        fullname=request.GET['fullname']
#        salary=request.GET['salary']
#        job=request.GET['job']
#        print("request params",fullname,salary,job)
 #       con=sqlite3.connect(r"/home/gundapu/Python/sqlite-tools-linux-x86-3310100/hr.db")
#        cur=con.cursor()
#        cur.execute("insert into employees(fullname,salary,job) values(?,?,?)",(fullname,salary,job))
#        con.commit()
#        con.close()
#        return render(request,'add_employee.html')

#def update_employee(request):
    #ids=request.GET['ids']
    #print(ids)
    #salary=request.GET['salary']
    #print("ids and salary",ids,salary)
    #query="update employees set salary="+salary +" where id="+ids
    #print("my query is",query)
    #con=sqlite3.connect(r"/home/gundapu/Python/sqlite-tools-linux-x86-3310100/hr.db")
    #cur=con.cursor()
    #cur.execute(query)
    #con.commit()
    #con.close()
   # return render(request,'update_employee.html')

def addemployee(request):
    if request.method=="POST":
        fullname=request.POST['fullname']
        print(fullname)
        salary=request.POST['salary']
        print(salary)
        job=request.POST['job']
        print(job)
        query="insert into employees(fullname,job,salary) values(?,?,?)",(fullname,job,salary)
        con=sqlite3.connect(r"/home/gundapu/Python/sqlite-tools-linux-x86-3310100/hr.db")
        cur=con.cursor()
        cur.execute("insert into employees(fullname,job,salary) values(?,?,?)",(fullname,job,salary))
        con.commit()
        con.close()
        return redirect("/hr/employees")
    else:
        return render(request,'addemployee.html')


def updateemployee(request):
    if request.method=="POST":

       salary=request.POST['salary']
       print(salary)
       ids=request.POST['ids']
       print("id",ids)
       salary=request.POST['salary']
       con=sqlite3.connect(r"/home/gundapu/Python/sqlite-tools-linux-x86-3310100/hr.db")
       query="update employees set salary="+salary+" where id="+ids
       print(query)
       cur=con.cursor()
       cur.execute(query)
       con.commit()
       con.close()
       return render(request,'updateemployee.html',{"message":"updated Employee"})
    else:
       return render(request,'updateemployee.html')
