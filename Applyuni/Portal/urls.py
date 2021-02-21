from django.contrib import admin
from django.urls import path,include
from .views.mediator import home
from .views.studentsignup import studentsignup
from .views.studentlogin import studentlogin
from .views.stdportal import stdnav
from .views.stdportal import stdsaved
from .views.stdportal import stduni
from .views.stdportal import stdsupport
from .views.stdportal import stdappl


urlpatterns=[
path('',home,name='home'),
path('studentsignup',studentsignup.as_view(),name='studentsignup'),
path('studentlogin',studentlogin.as_view(),name='studentloginpage'),
path('stdnav',stdnav,name='stdnav'),
path('stdsaved',stdsaved,name='stdsaved'),
path('stduni',stduni,name='stduni'),
path('stdsupport',stdsupport,name='stdsupport'),
path('stdappl',stdappl,name='stdappl'),

]