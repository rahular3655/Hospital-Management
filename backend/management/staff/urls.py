from django.urls import path
from .views import *



urlpatterns = [
    path('doctorcreate/', DoctorCreate.as_view(), name='doctorcreate'),
    path('doctor/<int:id>/', DoctorDetail.as_view(), name='doctordetail'),
    path('doctorlist/', ListDoctor.as_view(), name='doctorlist'),
    
    
    path('nursecreate/', NurseCreate.as_view(), name='nursecreate'),
    path('nurse/<int:id>/', NurseDetail.as_view(), name='nursedetail'),
    path('nurselist/', ListNurse.as_view(), name='nurselist'),
    
    
    path('attenderscreate/', AttendersCreate.as_view(), name='attenderscreate'),
    path('attenders/<int:id>/', AttendersDetail.as_view(), name='attendersdetail'),
    path('attenderslist/', ListAttenders.as_view(), name='attenderslist'),
]
