from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "signup_forms/studentlogin.html"
    def get(self,request):
        print("nanda")
        #return render(request,'Admin_portal/stddetail.html')
        return redirct('home')