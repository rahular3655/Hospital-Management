from django.db import models
from staff.models import *
from patients.models import *
# Create your models here.






class Patients(models.Model):
    
    STATUS=(
        ('Diagnosis','Diagnosis'),
        ('Admitted','Admitted'),
        ('Discharged','Discharged'),
    )
    
    name=models.CharField(max_length=200)
    age=models.CharField(max_length=10)
    address=models.CharField(max_length=500)
    phone = models.CharField(max_length=15)
    status= models.CharField(max_length=100,null=True,choices=STATUS,default="Diagnosis")
    admitted=models.BooleanField(default=False)
    time=models.DateField(auto_now_add=True)
    doctors=models.ManyToManyField(Doctor,null=True,default="OP")
    alloted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class MedicalConditions(models.Model):
    condition=models.CharField(max_length=1000 )
    detail=models.CharField(max_length=2000,null=True)
    testreports=models.CharField(max_length=150)
    datetime=models.DateTimeField( auto_now_add=True)
    patient=models.ManyToManyField(Patients,related_name="patient",null=True)
    
    def __str__(self):
        return self.patient.name


        
