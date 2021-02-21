from django.db import models
from django.core.validators import MinLengthValidator

class Stddetail(models.Model):
    
    Firstname= models.CharField(max_length=500)
    Lastname= models.CharField(max_length=500)
    Dateofbirth=models.CharField(max_length=50,null=True)
    Gender=models.CharField(max_length=50,null=True)
    Maritial=models.CharField(max_length=50,null=True)
    Nationality=models.CharField(max_length=50)
    Email = models.EmailField()
    Address=models.CharField(max_length=50)
    City=models.CharField(max_length=50)
    State=models.CharField(max_length=50)
    Country=models.CharField(max_length=50)
    Phonenumber= models.CharField(max_length=50)
    #sscgrading=(('M','Marks'),('%','Percentage'),('C','CGPA'))
    Sscqual=models.CharField(max_length=50)
    Sscname=models.CharField(max_length=50)
    Sscdate=models.CharField(max_length=10,null=True)
    Sscmarks=models.CharField(max_length=10)
    Sscgrading=models.CharField(max_length=50,null=True)
    SscDoc=models.FileField(upload_to="")
    #Intgrading=(('M','Marks'),('%','Percentage'),('C','CGPA'))
    Intqual=models.CharField(max_length=50)
    Intname=models.CharField(max_length=50)
    Intdate=models.CharField(max_length=10,null=True)
    Intmarks=models.CharField(max_length=10)
    Intgrading=models.CharField(max_length=50,null=True)
    IntDoc=models.FileField(upload_to="")
    #Unigrading=(('M','Marks'),('%','Percentage'),('C','CGPA'))
    Uniqual=models.CharField(max_length=50)
    Uniname=models.CharField(max_length=50)
    Unicname=models.CharField(max_length=50)
    Unidate=models.CharField(max_length=10,null=True)
    Unimarks=models.CharField(max_length=10)
    Unigrading=models.CharField(max_length=50,null=True)
    UniDoc=models.FileField(upload_to="")

    #testeng=(('I','IELTS'),('T','TOEFL'))
    #testad=(('G','GRE'),('GM','GMAT'))
    Testeng=models.CharField(max_length=50,null=True)
    Yeareng=models.CharField(max_length=10)
    Overallscoreeng=models.CharField(max_length=10)
    Uploadeng=models.FileField(upload_to="")

    Testeng1=models.CharField(max_length=50,null=True)
    Yeareng1=models.CharField(max_length=10)
    Overallscoreeng1=models.CharField(max_length=10)
    Uploadeng1=models.FileField(upload_to="")

    Testad=models.CharField(max_length=50,null=True)
    Yearad=models.CharField(max_length=10)
    Overallscoread=models.CharField(max_length=10)
    Uploadad=models.FileField(upload_to="")

    Testad1=models.CharField(max_length=50,null=True)
    Yearad1=models.CharField(max_length=10)
    Overallscoread1=models.CharField(max_length=10)
    Uploadad1=models.FileField(upload_to="")

    #applyingfor=(('B','Bachelors'),('M','Masters'))
    Applyingfor=models.CharField(max_length=50,null=True)
    Date=models.CharField(max_length=50)
    pcoun1=models.CharField(max_length=50)
    pcoun2=models.CharField(max_length=50)
    pcoun3=models.CharField(max_length=50)
    pcour4=models.CharField(max_length=50)
    pcour5=models.CharField(max_length=50)
    pcour6=models.CharField(max_length=50)

    def __str__(self):
        return self.Firstname
    def register(self):
        self.save()
        return True


    @staticmethod

    def get_stddetail_by_email(Email):
            #print(Email)
            #print(Stddetail.objects.all())
            #print(Stddetail.objects.get(Email=Email))
            try:
                return Stddetail.objects.get(Email=Email)
            except:
                False
