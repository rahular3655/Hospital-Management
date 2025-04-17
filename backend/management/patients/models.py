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
    status= models.CharField(max_length=100,blank=True,choices=STATUS,default="Diagnosis")
    admitted=models.BooleanField(default=False)
    time=models.DateField(auto_now_add=True)
    doctors=models.ManyToManyField(Doctor,null=True,default="OP",related_name="patients")
    is_alloted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class MedicalConditions(models.Model):
    patient=models.ForeignKey(Patients,related_name="medical_conditions",null=True,on_delete=models.CASCADE)
    condition=models.CharField(blank=True,max_length=1000 )
    detail=models.CharField(blank=True,max_length=2000,null=True)
    testreports=models.CharField(blank=True,max_length=150)
    datetime=models.DateTimeField( auto_now_add=True)
    
    def __str__(self):
        return self.patient.name


class Medications(models.Model):
    patient = models.ForeignKey(Patients,related_name="medicine",on_delete=models.CASCADE)
    prescribed_by  = models.ForeignKey(Doctor,related_name="medicine",on_delete=models.CASCADE)
    name_of_medicine = models.TextField(null=True,blank=True)     
