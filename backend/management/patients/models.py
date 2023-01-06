from django.db import models
from staff.models import *
# Create your models here.




class Patients(models.Model):
    
    STATUS=(
        ('Diagnosis','Diagnosis'),
        ('Admitted','Admitted'),
        ('Discharge','Discharge'),
    )
    
    name=models.CharField(max_length=200)
    age=models.CharField(max_length=10)
    address=models.CharField(max_length=500)
    phone = models.CharField(max_length=15)
    status= models.CharField(max_length=100,null=True,choices=STATUS,default="Diagnosis")
    admitted=models.BooleanField(default=False)
    medical_condition=models.CharField(max_length=1000)
    time=models.DateField(auto_now_add=True)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE,null=True,default="OP")
    alloted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    
class MedicalConditions(models.Model):
    patient=models.ForeignKey(Patients,on_delete=models.CASCADE)
    condition=models.CharField(max_length=1000)
    testreports=models.CharField(max_length=150)
    datetime=models.DateTimeField( auto_now_add=True)
    
    def __str__(self):
        return self.patient.name
        
        
