from django.contrib import admin
from .models import BloodGroup,Role,DropDownClass,DropDown

# Register your models here.

admin.site.register(BloodGroup)
# admin.site.register(Role)
admin.site.register(DropDown)
admin.site.register(DropDownClass)