from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from Portal.models.studentinfo import Student
from django.views import View
from django.shortcuts import render,redirect
class studentsignup(View):
    def get(self,request):
        return render(request,'signup_forms/studentlogin.html')
    def post(self,request):
        postData = request.POST
        Firstname=postData.get('Firstname')
        Email=postData.get('Email')
        Password=postData.get('Password')
        Confirmpassword=postData.get('Confirmpassword')
        print(Firstname)

        error_message=None
        studentsignup1=Student.IsExists(Email)
        value={'Firstname':Firstname,'Email':Email,'Password':Password,'Confirmpassword':Confirmpassword}


        print(Email)
        if(studentsignup1):
            error_message="Email already Exists !!"
            data={'value':value , 'error': error_message}
            return render(request,'signup_forms/studentlogin.html',data)
        if(Password !=Confirmpassword ):
            error_message="Password is not valid"
            data={'value':value , 'error': error_message}
            return render(request,'signup_forms/studentlogin.html',data)

        print(Password)

        studentsignup=Student(Firstname =Firstname,Email=Email,
        Password=Password,Confirmpassword=Confirmpassword )
        studentsignup.Password=make_password(studentsignup.Password)
        studentsignup.Confirmpassword=make_password(studentsignup.Confirmpassword)
        studentsignup.register()
        print("aaaaaa")
        return redirect('home')
