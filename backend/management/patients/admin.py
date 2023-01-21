from django.contrib import admin
from .models import *
# Register your models here.


class Patientadmin(admin.ModelAdmin):
    list_display=['name']

admin.site.register(Patients)
admin.site.register(MedicalConditions)