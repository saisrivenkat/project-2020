from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from Portal.models.studentinfo import Student
from django.views import View
from django.contrib.auth.hashers import make_password
import smtplib
import random
import string
a=""

class temp_pass:
    def do(Email):
        global a
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login('techclub.cse.sse@gmail.com','techclubcse@saveetha')
        letters=string.ascii_lowercase
        a=str(''.join(random.choice(letters) for i in range(10)))
        print(a)
        b=a+'    '+'Use this as Your Temporary Password'
        print(a,"nanda")
        server.sendmail('techclub.cse.sse@gmail.com',Email,b)
        return a

class emailvalid(View):
    def get(self,request):
        return render(request,'signup_forms/password_reset.html')
    def post(self,request):
        Email=request.POST.get('Email')
        request.session['Email']=Email
        a1=Student.IsExists(Email)
        if(a1):
            if(temp_pass.do(Email)):
                error_message="Email has been sent successfully"
                return render(request,'signup_forms/password_reset.html',{'error':error_message})
        else:
            error_message1="Please Enter Valid Email"
            return render(request,'signup_forms/password_reset.html',{'error1':error_message1})
class tempvalidator(View):
    def get(self,request):
        return render(request,'signup_forms/password_reset_confirm.html')
    def post(self,request):

        temp_pass=request.POST.get('temp_pass')
        Password=request.POST.get('Password')
        Confirmpassword=request.POST.get('Confirmpassword')
        student=Student.get_student_by_email(request.session['Email'])
        #student.Password=None
        print(temp_pass)
        print(a)
        if(temp_pass==a):
            print("nanda")
            student.Password=make_password(Password)
            student.Confirmpassword=make_password(Confirmpassword)
            #student.temp_pass=None
            student.register()
            print(student.Password)
            request.session.clear()
            return render(request,'signup_forms/studentlogin.html')
        else:
            error_message2="Please Enter Valid Temporary Password"
            return render(request,'signup_forms/password_reset_confirm.html',{'error2':error_message2})
