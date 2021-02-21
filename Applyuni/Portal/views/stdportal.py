from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.views import View

#def stdhome(request):
    #return render(request,'student_portal/studenthome.html',data)
def stdhome(request):
    return render(request,'Student_portal/stdhome.html')
def stdnav(request):
    return render(request,'Student_portal/navbar.html')
def stduni(request):
    return render(request,'Student_portal/universities.html')
def stdsupport(request):
    return render(request,'Student_portal/support.html')
def stdsaved(request):
    return render(request,'Student_portal/saved_university.html')
def stdappl(request):
    return render(request,'Student_portal/applications.html')
