from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.views import View

def Detail(request):
    return render(request,'Student_portal/Detail_Application.html')