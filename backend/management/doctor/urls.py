from .views import *
from django.urls import path



urlpatterns = [
    path('doctordetail/', doctorProfile.as_view(), name='doctordetail'),
    path('doctorpatientdetail/', doctor_patient_list.as_view(), name='doctorpatientdetail'),
]
