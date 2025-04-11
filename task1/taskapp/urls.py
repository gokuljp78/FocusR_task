from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views

 
urlpatterns=[
    path('',views.ret,name="project")    ,
    path('2/<str:pk>/',views.ret2,name="project") 
]
