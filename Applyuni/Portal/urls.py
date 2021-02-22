from django.contrib import admin
from django.urls import path,include
from .views.mediator import home
from .views.mediator import appli
from .views.studentsignup import studentsignup
from .views.studentlogin import studentlogin
from .views.studentlogin import logout

from .views.stdportal import stdhome


from .views.stdportal import stdnav
from .views.stdportal import stdsaved
from .views.stdportal import stduni
from .views.stdportal import stdsupport
from .views.stdportal import stdappl


from .views.stdprofile import stdacd
from .views.stdprofile import stdcour
from .views.stdprofile import stdind
from .views.stdprofile import stdpro

from .views.temp_pass import emailvalid
from .views.temp_pass import tempvalidator

urlpatterns=[
path('',home,name='home'),
path('appli',appli,name='appli'),
path('studentsignup',studentsignup.as_view(),name='studentsignup'),
path('studentlogin',studentlogin.as_view(),name='studentloginpage'),
path('logout',logout,name='logout'),

path('stdhome',stdhome,name='stdhome'),
path('stdnav',stdnav,name='stdnav'),
path('stdsaved',stdsaved,name='stdsaved'),
path('stduni',stduni,name='stduni'),

path('stdsupport',stdsupport,name='stdsupport'),
path('stdappl',stdappl,name='stdappl'),
path('stdacd',stdacd.as_view(),name='stdacd'),
path('stdcour',stdcour.as_view(),name='stdcour'),
path('stdind',stdind.as_view(),name='stdind'),
path('stdpro',stdpro.as_view(),name='stdpro'),

path('emailvalid',emailvalid.as_view(),name='emailvalid'),
path('tempvalidator',tempvalidator.as_view(),name='tempvalidator'),

]