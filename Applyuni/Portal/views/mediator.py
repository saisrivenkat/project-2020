from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse

def home(request):
    return render(request,'landing_page.html')