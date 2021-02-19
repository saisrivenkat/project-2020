from django.contrib import admin
from django.urls import path,include
from .views.mediator import home
from .views.studentsignup import studentsignup
from .views.studentlogin import studentlogin
urlpatterns=[
path('',home,name='home'),
path('studentsignup',studentsignup.as_view(),name='studentsignup'),
path('studentlogin',studentlogin.as_view(),name='studentloginpage'),
]