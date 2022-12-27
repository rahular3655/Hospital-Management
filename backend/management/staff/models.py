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
    phonenumber=models.IntegerField(null=True)
    bloodGroup=models.CharField(max_length=5,null=True)
    age=models.IntegerField(null=False)
    status=models.CharField(max_length=100,null=True,choices=STATUS,default="new")
    image=models.ImageField(upload_to='images/Doctors',null=False)
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

    
# class Security(models.Model):
#     name=models.CharField(max_length=150,null=False)
#     date_of_join=models.DateField(auto_now_add=False, null=False)
#     phonenumber=models.IntegerField(null=True)
#     bloodGroup=models.CharField(max_length=5,null=True)
#     age=models.IntegerField(null=False)
#     image=models.ImageField(upload_to='images/Security',null=False)
    
#     def __str__(self):
#         return self.name
    
# class Attenders(models.Model):
#     name=models.CharField(max_length=150,null=False)
#     date_of_join=models.DateField(auto_now_add=False, null=False)
#     phonenumber=models.IntegerField(null=True)
#     bloodGroup=models.CharField(max_length=5,null=True)
#     age=models.IntegerField(null=False)
#     image=models.ImageField(upload_to='images/Attenders',null=False)
    
#     def __str__(self):
#         return self.name
    
# class Receptionist(models.Model):
#     name=models.CharField(max_length=150,null=False)
#     date_of_join=models.DateField(auto_now_add=False, null=False)
#     phonenumber=models.IntegerField(null=True)
#     bloodGroup=models.CharField(max_length=5,null=True)
#     age=models.IntegerField(null=False)
#     image=models.ImageField(upload_to='images/Receptionist',null=False)
    
#     def __str__(self):
#         return self.name
    
# class Managers(models.Model):
#     name=models.CharField(max_length=150,null=False)
#     date_of_join=models.DateField(auto_now_add=False, null=False)
#     phonenumber=models.IntegerField(null=True)
#     bloodGroup=models.CharField(max_length=5,null=True)
#     age=models.IntegerField(null=False)
#     image=models.ImageField(upload_to='images/Managers',null=False)
    
#     def __str__(self):
#         return self.name
    
# class Labassistant(models.Model):
#     name=models.CharField(max_length=150,null=False)
#     date_of_join=models.DateField(auto_now_add=False, null=False)
#     phonenumber=models.IntegerField(null=True)
#     bloodGroup=models.CharField(max_length=5,null=True)
#     age=models.IntegerField(null=False)
#     image=models.ImageField(upload_to='images/Labassistant',null=False)
    
#     def __str__(self):
#         return self.name

# class Helpers(models.Model):
#     name=models.CharField(max_length=150,null=False)
#     date_of_join=models.DateField(auto_now_add=False, null=False)
#     phonenumber=models.IntegerField(null=True)
#     bloodGroup=models.CharField(max_length=5,null=True)
#     age=models.IntegerField(null=False)
#     image=models.ImageField(upload_to='images/Helpers',null=False)
    
#     def __str__(self):
#         return self.name

# class Others(models.Model):
#     name=models.CharField(max_length=150,null=False)
#     date_of_join=models.DateField(auto_now_add=False, null=False)
#     designation=models.CharField(max_length=150,null=True)
#     phonenumber=models.IntegerField(null=True)
#     bloodGroup=models.CharField(max_length=5,null=True)
#     age=models.IntegerField(null=False)
#     image=models.ImageField(upload_to='images/others',null=False)
    
#     def __str__(self):
#         return self.name
    

# class Staff(models.Model):
#     doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
#     nurse=models.ForeignKey(Nurse,on_delete=models.CASCADE)
#     security=models.ForeignKey(Security,on_delete=models.CASCADE)
#     attenders=models.ForeignKey(Attenders,on_delete=models.CASCADE)
#     receptionist=models.ForeignKey(Receptionist,on_delete=models.CASCADE)
#     managers=models.ForeignKey(Managers,on_delete=models.CASCADE)
#     labassistant=models.ForeignKey(Labassistant,on_delete=models.CASCADE)
#     helpers=models.ForeignKey(Helpers,on_delete=models.CASCADE)
#     others=models.ForeignKey(Others,on_delete=models.CASCADE)
    
    