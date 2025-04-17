from django.db import models
from userapi.models import *
from django.utils.text import slugify

# Create your models here.


class DoctorChoices(models.TextChoices):
    new = ('new','new')
    senior = ('senior','Senior')
    experienced = ('experienced','Experienced')
    
class NursesChoices(models.TextChoices):
    new = ('new','new')
    senior = ('Senior','Senior')
    head_nurse = ('HeadNurse','HeadNurse')
    
class StaffChoices(models.TextChoices):
    security = ('Security','Security')
    attender = ('Attender','Attender')
    receptionist = ('Receptionist','Receptionist')
    manager = ('Manager','Manager')
    labassistant = ('Labassistant','Labassistant')
    helper = ('Helper','Helper')
    
class WorkShift(models.TextChoices):
    day = ('day','Day')
    night = ('night','Night')
    off = ('off','Off')
    leave = ('leave','Leave')
    absent = ('absent','Absent')
    
class LeaveApplicationChoices(models.TextChoices):
    waiting = ('waiting','Waiting')
    approved  = ('approved','Approved')
    rejected =  ('rejected','Rejected')
    
class Doctor(models.Model):

    user=models.ForeignKey(Account,on_delete=models.CASCADE,related_name="doctor")
    name=models.CharField(max_length=150,null=False)
    slug = models.SlugField(max_length=100, unique=True, blank=False, null=True)
    date_of_join=models.DateField(auto_now_add=False, null=False)
    specialized_in=models.CharField(max_length=150,null=True)
    phonenumber=models.CharField(max_length=15,null=True)
    blood_group=models.CharField(max_length=5,null=True)
    age=models.CharField(max_length=6,null=False)
    status=models.CharField(max_length=100,blank=True,choices=DoctorChoices.choices,default="new")
    image=models.ImageField(upload_to='images/Doctors',null=True)
    shift = models.CharField(max_length=100,blank=True,choices=WorkShift.choices)
    is_available = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
        
class Nurse(models.Model):
    
    user=models.ForeignKey(Account,on_delete=models.CASCADE,related_name="nurse")
    name=models.CharField(max_length=150,null=False)
    date_of_join=models.DateField(auto_now_add=False, null=False)
    phonenumber=models.IntegerField(null=True)
    bloodGroup=models.CharField(max_length=5,null=True)
    age=models.IntegerField(null=False)
    status=models.CharField(max_length=100,null=True,choices=NursesChoices.choices,default="new")
    image=models.ImageField(upload_to='images/Nurse',null=False)
    created_by = models.ForeignKey(Account, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
    
class StaffForms(models.Model):
    
    name=models.CharField(max_length=150,null=False)
    date_of_join=models.DateField(auto_now_add=False, null=False)
    phonenumber=models.IntegerField(null=True)
    bloodGroup=models.CharField(max_length=5,null=True)
    age=models.IntegerField(null=False)
    image=models.ImageField(upload_to='images/staffs',null=False)
    status=models.CharField(max_length=120,null=False,choices=StaffChoices.choices)
    created_by = models.ForeignKey(Account, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.name

    
class LeaveApplication(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE,null=True,related_name="leave_application")
    subject = models.TextField(blank=True)
    date_of_leave = models.DateField(blank=False)
    is_medical_leave = models.BooleanField(default=False)
    is_emergency = models.BooleanField(default=True)
    is_approved = models.CharField(default="Waiting",choices=LeaveApplicationChoices.choices)
    
    