from django.db import models
from django.contrib.auth.models import User

# Create your models here.


    
    
class Doctor(models.Model):
    STATUS=(
        ('new','new'),
        ('Senior','Senior'),
        ('Experienced','Experienced'),
    )
    name=models.CharField(max_length=150,null=False)
    date_of_join=models.DateField(auto_now_add=False, null=False)
    specialized_in=models.CharField(max_length=150,null=True)
    phonenumber=models.CharField(max_length=15,null=True)
    bloodGroup=models.CharField(max_length=5,null=True)
    age=models.CharField(max_length=6,null=False)
    status=models.CharField(max_length=100,null=True,choices=STATUS,default="new")
    image=models.ImageField(upload_to='images/Doctors',null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
        
class Nurse(models.Model):
    STATUS=(
        ('new','new'),
        ('Senior','Senior'),
        ('HeadNurse','HeadNurse'),
    )
    name=models.CharField(max_length=150,null=False)
    date_of_join=models.DateField(auto_now_add=False, null=False)
    phonenumber=models.IntegerField(null=True)
    bloodGroup=models.CharField(max_length=5,null=True)
    age=models.IntegerField(null=False)
    status=models.CharField(max_length=100,null=True,choices=STATUS,default="new")
    image=models.ImageField(upload_to='images/Nurse',null=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
    
class StaffForms(models.Model):
    STATUS=(
        ('Security','Security'),
        ('Attender','Attender'),
        ('Receptionist','Receptionist'),
        ('Manager','Manager'),
        ('Labassistant','Labassistant'),
        ('Helper','Helper'),
    )
    name=models.CharField(max_length=150,null=False)
    date_of_join=models.DateField(auto_now_add=False, null=False)
    phonenumber=models.IntegerField(null=True)
    bloodGroup=models.CharField(max_length=5,null=True)
    age=models.IntegerField(null=False)
    image=models.ImageField(upload_to='images/staffs',null=False)
    status=models.CharField(max_length=120,null=True,choices=STATUS)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.name    

    

    
    