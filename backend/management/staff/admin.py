from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(DoctorProfile)
admin.site.register(NurseProfile)
admin.site.register(StaffProfile)
admin.site.register(Role)
admin.site.register(LeaveApplication)