from django.urls import path
from . import views
urlpatterns = [ 
        #path('index', views.index, name='index'),
        #path('hello/', views.hello),
        path('welcome/', views.welcome),
        path('index/', views.index),
        path('employees/', views.list_employees),
        path('countries/', views.countriesnandp),
        #path('add_employee/',views.add_employee),
        #path('update_employee', views.update_employee),
        path('addemployee/', views.addemployee),
        path('updateemployee/', views.updateemployee),
        ]
