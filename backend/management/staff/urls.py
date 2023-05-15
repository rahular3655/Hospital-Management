from django.urls import path
from .views import *



urlpatterns = [
    path('doctorcreate/', DoctorCreate.as_view(), name='doctorcreate'),
    path('doctor/<int:id>/', DoctorDetail.as_view(), name='doctordetail'),
    path('doctorlist/', ListDoctor.as_view(), name='doctorlist'),
    path('fddoctorlist/', DoctorList.as_view(), name='fddoctorlist'),
    
    
    path('nursecreate/', NurseCreate.as_view(), name='nursecreate'),
    path('nurse/<int:id>/', NurseDetail.as_view(), name='nursedetail'),
    path('nurselist/', ListNurse.as_view(), name='nurselist'),
    
    
    
    path('staffcreate/',StaffCreate.as_view(),name='staffcreate'),
    path('staffdetail/<int:id>/',StaffDetail.as_view(),name='staffdetail'),
    path('stafflist/',Stafflist.as_view(),name='stafflist'),
    
]
