from django.db import models
from patients.models import *

# Create your models here.



class Block (models.Model):
    
    name=models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.name
    

class Floors (models.Model):
    name =models.CharField(max_length=100,null=True)
    blockname=models.ForeignKey(Block , on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.name 
    
class Bed (models.Model):
    name=models.CharField(max_length=100,null=True)
    floor = models.ForeignKey(Floors,on_delete=models.CASCADE,null=True)
    reserved_by=models.ForeignKey(Patients,on_delete=models.CASCADE,null=True)
    is_available=models.BooleanField(default=True)    
    def __str__(self):
        return self.name
    
class Machines(models.Model):
    STATUS=(('Working','Working'),
            ('Repair','Repair'),
            ('Fixed','Fixed'))
    name=models.CharField(max_length=100,null=True)
    Floor=models.ManyToManyField(Floors,null=True)
    Condition=models.CharField(max_length=100,choices=STATUS,null=True)
    
    
    