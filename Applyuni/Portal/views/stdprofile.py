from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.views import View


def stdacd(request):
    return render(request,'Contactform_v9/academic.html')
def stdcour(request):
    return render(request,'Contactform_v9/course.html')
def stdind(request):
    return render(request,'Contactform_v9/index.html')
def stdpro(request):
    return render(request,'Contactform_v9/professional.html')