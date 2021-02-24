from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.views import View
from django.core.files.storage import FileSystemStorage
from Portal.models.stddetail import Stdacd,Stdpro,Stdind,Stdcour,Stdpro1
from Portal.models.studentinfo import Student

class stdind(View):
    def get(self,request):
        data={}
        print(request.session['Email'])
        student=Student.get_student_by_email(request.session['Email'])
        qwe="rty"
        print(student)
        print(qwe)
        if(student):
            stdind=Stdind.get_stdind_by_email(student.Email)
        print(stdind)
        if(stdind):
            value={'Firstname': stdind.Firstname,'Lastname': stdind.Lastname,'Dateofbirth':stdind.Dateofbirth,'Gender':stdind.Gender,
                'Maritial':stdind.Maritial,'Nationality':stdind.Nationality,'Email' : stdind.Email,'Address':stdind.Address,'City':stdind.City,'State':stdind.State,
                'Country':stdind.Country,'Phonenumber': stdind.Phonenumber}
            data={'value':value}

        return render(request,'Contactform_v9/index.html',data)
    def post(self,request):
        print("hiii")
        Firstname= request.POST.get('Firstname')
        Lastname= request.POST.get('Lastname')
        Dateofbirth=request.POST.get('Dateofbirth')
        print(Firstname)
        Gender=request.POST.get('Gender')
        Maritial=request.POST.get('Maritial')
        Nationality=request.POST.get('Nationality')
        Email = request.POST.get('Email')
        Address=request.POST.get('Address')
        City=request.POST.get('City')
        State=request.POST.get('State')
        Country=request.POST.get('Country')
        Phonenumber= request.POST.get('Phonenumber')
        if(Email!=request.session['Email']):
            error_message="ohh your email doesn't matched with login mail"
            return render(request,'Contactform_v9/index.html',{error:error_message})
        else:
            student=Student.get_student_by_email(Email)
            stdind1=Stdind.get_stdind_by_email(student.Email)
            if(City==None or Country == None):
                City=Stdind1.City
                Country=Stdind1.Country
            stdind=Stdind(Firstname= Firstname,Lastname= Lastname,Dateofbirth=Dateofbirth,Gender=Gender,
            Maritial=Maritial,Nationality=Nationality,Email = Email,Address=Address,City=City,State=State,
            Country=Country,Phonenumber= Phonenumber)
            if(stdind1):
                stdind1.delete()
            stdind.register()
            value={'Firstname': Firstname,'Lastname': Lastname,'Dateofbirth':Dateofbirth,'Gender':Gender,
            'Maritial':Maritial,'Nationality':Nationality,'Email' : Email,'Address':Address,'City':City,'State':State,
            'Country':Country,'Phonenumber': Phonenumber}
            data={'value':value}
            return render(request,'Contactform_v9/index.html',data)

class stdacd(View):
    def get(self,request):
        data={}
        student=Student.get_student_by_email(request.session['Email'])
        if(student):
            stdacd=Stdacd.get_stdacd_by_email(student.Email)
        if(stdacd):
            value={'Sscqual':stdacd.Sscqual,'Sscname':stdacd.Sscname,'Sscdate':stdacd.Sscdate,'Sscmarks':stdacd.Sscmarks,'Sscgrading':stdacd.Sscgrading,'SscDoc':stdacd.SscDoc,
                'Intqual':stdacd.Intqual,'Intname':stdacd.Intname,'Intdate':stdacd.Intdate,'Intmarks':stdacd.Intmarks,'Intgrading':stdacd.Intgrading,
                'IntDoc':stdacd.IntDoc,'Uniqual':stdacd.Uniqual,'Uniname':stdacd.Uniname,'Unicname':stdacd.Unicname,'Unidate':stdacd.Unidate,'Unimarks': stdacd.Unimarks,
                'Unigrading':stdacd.Unigrading,'UniDoc':stdacd.UniDoc}
            data={'value':value}
        return render(request,'Contactform_v9/academic.html',data)
    def post(self,request):
        print("in post man in stddetail")
        Email=request.session['Email']
        Sscqual=request.POST.get('Sscqual')
        print("123456")
        print(Sscqual)
        Sscname=request.POST.get('Sscname')
        Sscdate=request.POST.get('Sscdate')
        Sscmarks=request.POST.get('Sscmarks')
        Sscgrading=request.POST.get('Sscgrading')
        SscDoc=request.FILES['SscDoc']

        fs=FileSystemStorage()
        name=fs.save(SscDoc.name,SscDoc)
        url=fs.url(name)
        print(url)
        Intqual=request.POST.get('Intqual')
        Intname=request.POST.get('Intname')
        Intdate=request.POST.get('Intdate')
        Intmarks=request.POST.get('Intmarks')
        Intgrading=request.POST.get('Intgrading')
        IntDoc=request.FILES['IntDoc']

        name1=fs.save(IntDoc.name,IntDoc)
        url1=fs.url(name1)
        Uniqual=request.POST.get('Uniqual')
        Uniname=request.POST.get('Uniname')
        Unicname=request.POST.get('Unicname')
        Unidate=request.POST.get('Unidate')
        Unimarks=request.POST.get('Unimarks')
        Unigrading=request.POST.get('Unigrading')
        UniDoc=request.FILES['UniDoc']

        name2=fs.save(UniDoc.name,UniDoc)
        url2=fs.url(name2)
        stdacd=Stdacd(Email=Email,Sscqual=Sscqual,Sscname=Sscname,Sscdate=Sscdate,Sscmarks=Sscmarks,Sscgrading=Sscgrading,SscDoc=SscDoc,
            Intqual=Intqual,Intname=Intname,
            Intdate=Intdate,
            Intmarks=Intmarks,Intgrading=Intgrading,IntDoc=IntDoc,Uniqual=Uniqual,Uniname=Uniname,Unicname=Unicname
            ,Unidate=Unidate,Unimarks=Unimarks,Unigrading=Unigrading,UniDoc=UniDoc)

        student=Student.get_student_by_email(Email)
        stdacd1=Stdacd.get_stdacd_by_email(student.Email)
        if(stdacd1):
            stdacd1.delete()
        stdacd.register()
        value={'Sscqual':Sscqual,'Sscname':Sscname,'Sscdate':Sscdate,'Sscmarks':Sscmarks,'Sscgrading':Sscgrading,'SscDoc':url,
            'Intqual':Intqual,'Intname':Intname,'Intdate':Intdate,'Intmarks':Intmarks,'Intgrading':Intgrading,
            'IntDoc':url1,'Uniqual':Uniqual,'Uniname':Uniname,'Unicname':Unicname,'Unidate':Unidate,'Unimarks': Unimarks,
            'Unigrading':Unigrading,'UniDoc':url2}
        data={'value':value}
        return render(request,'Contactform_v9/academic.html',data)
class stdcour(View):
    def get(self,request):
        data={}
        student=Student.get_student_by_email(request.session['Email'])
        if(student):
            stdcour=Stdcour.get_stdcour_by_email(student.Email)
        if(stdcour):
            value={'Applyingfor':stdcour.Applyingfor,'Date':stdcour.Date,'pcoun1':stdcour.pcoun1,'pcoun2':stdcour.pcoun2,'pcoun3':stdcour.pcoun3,'pcour4':stdcour.pcour4,'pcour5':stdcour.pcour5,'pcour6':stdcour.pcour6}
            data={'value':value}
        return render(request,'Contactform_v9/course.html',data)
    def post(self,request):
        Email=request.session['Email']
        Applyingfor=request.POST.get('Applyingfor')
        Date=request.POST.get('Date')
        pcoun1=request.POST.get('pcoun1')
        pcoun2=request.POST.get('pcoun2')
        pcoun3=request.POST.get('pcoun3')
        pcour4=request.POST.get('pcour4')
        pcour5=request.POST.get('pcour5')
        pcour6=request.POST.get('pcour6')

        print(pcoun1)

        stdcour=Stdcour(Applyingfor=Applyingfor,Date=Date,pcoun1=pcoun1,pcoun2=pcoun2,
        pcoun3=pcoun3,pcour4=pcour4,pcour5=pcour5,pcour6=pcour6,Email=Email)
        student=Student.get_student_by_email(Email)
        stdcour1=Stdcour.get_stdcour_by_email(student.Email)
        if(stdcour1):
            stdcour1.delete()
        stdcour.register()
        value={'Applyingfor':Applyingfor,'Date':Date,'pcoun1':pcoun1,'pcoun2':pcoun2,'pcoun3':pcoun3,'pcour4':pcour4,'pcour5':pcour5,'pcour6':pcour6}
        data={'value':value}
        return render(request,'Contactform_v9/course.html',data)
class stdpro(View):
    def get(self,request):
        data={}
        student=Student.get_student_by_email(request.session['Email'])
        if(student):
            stdpro=Stdpro.get_stdpro_by_email(student.Email)
            stdpro1=Stdpro1.get_stdpro1_by_email(student.Email)
        if(stdpro):
            testeng=[]
            yeareng=[]
            overallscoreeng=[]
            uploadeng=[]
            for i in range(0,len(stdpro)):
                testeng.append(stdpro[i].Testeng)
                yeareng.append(stdpro[i].Yeareng)
                overallscoreeng.append(stdpro[i].Overallscoreeng)
                uploadeng.append(stdpro[i].Urleng)
            list=[]
            for i in range(0,len(stdpro)):
                list.append({'Testeng':testeng[i],
                         'Yeareng':yeareng[i],
                              'Overallscoreeng':overallscoreeng[i],
                                                  'Uploadeng':uploadeng[i]})
            
            data['stdpro']=list
        if(stdpro1):
            testad=[]
            yearad=[]
            overallscoread=[]
            uploadad=[]
            for i in range(0,len(stdpro1)):
                testad.append(stdpro1[i].Testad)
                yearad.append(stdpro1[i].Yearad)
                overallscoread.append(stdpro1[i].Overallscoread)
                uploadad.append(stdpro1[i].Urlad)
            list1=[]
            for i in range(0,len(stdpro1)):
                list1.append({'Testad':testad[i],
                         'Yearad':yearad[i],
                              'Overallscoread':overallscoread[i],
                                                  'Uploadad':uploadad[i]})
            data['stdpro1']=list1
            
        return render(request,'Contactform_v9/professional.html',data)
    def post(self,request):
        Email=request.session['Email']
        Testeng=request.POST.getlist('Testeng[]')
        Yeareng=request.POST.getlist('Yeareng[]')
        Overallscoreeng=request.POST.getlist('Overallscoreeng[]')

        Testad=request.POST.getlist('Testad[]')
        Yearad=request.POST.getlist('Yearad[]')
        Overallscoread=request.POST.getlist('Overallscoread[]')
        fs=FileSystemStorage()
        Uploadeng=request.FILES.getlist('Uploadeng[]')
        print(Testeng)
        print(Yeareng)
        print(Overallscoreeng)
        print(Uploadeng)
        print(Testad)
        print(Yearad)
        print(Overallscoread)
        Uploadad=request.FILES.getlist('Uploadad[]')
        print(Uploadad)
        urleng=[]
        urlad=[]
        for i in range(0,len(Testeng)):
            testeng=Testeng[i]
            yeareng=Yeareng[i]
            overallscoreeng=Overallscoreeng[i]
            uploadeng=Uploadeng[i]
            name=fs.save(uploadeng.name,uploadeng)
            url=fs.url(name)
            urleng.append(url)
            stdpro=Stdpro(Email=Email,Testeng=testeng,Yeareng=yeareng,Overallscoreeng=overallscoreeng,Uploadeng=uploadeng,Urleng=url)
            stdpro.register()

        for i in range(0,len(Testad)):
            testad=Testad[i]
            yearad=Yearad[i]
            overallscoread=Overallscoread[i]
            uploadad=Uploadad[i]
            name=fs.save(uploadad.name,uploadad)
            url=fs.url(name)
            urlad.append(url)
            stdpro1=Stdpro1(Email=Email,Testad=testad,Yearad=yearad,Overallscoread=overallscoread,Uploadad=uploadad,Urlad=url)
            stdpro1.register()


        '''name3=fs.save(Uploadeng.name,Uploadeng)
        url3=fs.url(name3)

        
        name5=fs.save(Uploadad.name,Uploadad)
        url5=fs.url(name5)
        
        print(url3)'''
        '''stdpro=Stdpro(Email=Email,Testeng=Testeng,Yeareng=Yeareng,Overallscoreeng=Overallscoreeng,Uploadeng=Uploadeng,
            Testad=Testad,Yearad=Yearad,Overallscoread=Overallscoread,Uploadad=Uploadad)
        stdpro.register()'''
        value={'Testeng': Testeng,'Yeareng':Yeareng,'Overallscoreeng': Overallscoreeng,'Uploadeng':urleng,
            'Testad': Testad,'Yearad': Yearad,'Overallscoread':Overallscoread,'Uploadad':urlad}
        data={'value':value}
        return redirect('stdhome')
