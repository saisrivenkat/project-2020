from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse

def home(request):
    return render(request,'index.html')
def appli(request):
    return render(request,'Student_portal/Detail_Application.html')