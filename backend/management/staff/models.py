from django.db import models
from accounts.models import User
from django.utils.text import slugify
from common.models import Role

# Create your models here.
     
class LeaveApplicationChoices(models.TextChoices):
    waiting = ('waiting','Waiting')
    approved  = ('approved','Approved')
    rejected =  ('rejected','Rejected')

class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    specialization = models.CharField(max_length=100, blank=True, null=True)
    license_number = models.CharField(max_length=50, blank=True, null=True)
    # Add other doctor-specific fields

    def __str__(self):
        return f"{self.user.get_full_name()} (Doctor)"

class NurseProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='nurse_profile')
    department = models.CharField(max_length=100, blank=True, null=True)
    registration_number = models.CharField(max_length=50, blank=True, null=True)
    # Add other nurse-specific fields

    def __str__(self):
        return f"{self.user.get_full_name()} (Nurse)"

class StaffProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='staff_profile')
    roles = models.ManyToManyField(Role, related_name='staff_profiles')
    # Add other staff-specific fields (that apply to all staff)

    def __str__(self):
        roles_str = ", ".join(role.name for role in self.roles.all())
        return f"{self.user.get_full_name()} (Staff: {roles_str})"
    
class LeaveApplication(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name="leave_application")
    subject = models.TextField(blank=True)
    date_of_leave = models.DateField(blank=False)
    is_medical_leave = models.BooleanField(default=False)
    is_emergency = models.BooleanField(default=True)
    is_approved = models.CharField(default="Waiting",choices=LeaveApplicationChoices.choices)
    
    