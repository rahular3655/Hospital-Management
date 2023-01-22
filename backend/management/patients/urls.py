from django.urls import path
from .views import *


urlpatterns = [
    path('patientcreate/', PatientCreate.as_view(), name='patientcreate'),
    path('patientlist/', PatientList.as_view(), name='patientlist'),
    path('createmdcntn/', MedicalCondition.as_view(), name='createmdcntn'),
    path('deletepatient/<int:id>/', DeletePatient.as_view(), name='deletepatient'),
    path('assignpatienttodoc/', AssignPatientToDoctor.as_view(), name='assignpatienttodoc'),
    path('admitpatient/', AdmitPatient.as_view(), name='admitpatient'),
]
