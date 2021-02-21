from django.db import models
from django.core.validators import MinLengthValidator

class Application(models.Model):
    Universityname=models.CharField(max_length=500)
    Coursename=models.CharField(max_length=500)
    Semno=models.CharField(max_length=500)
    Startdate=models.CharField(max_length=500)
    Enddate=models.CharField(max_length=500)
    Studentname=models.CharField(max_length=500)
    Nationality=models.CharField(max_length=500)
    Intake=models.CharField(max_length=500)
    Applydate=models.DateField(max_length=50)
    Status=models.CharField(max_length=500)
