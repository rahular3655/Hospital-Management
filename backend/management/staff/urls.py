from django.urls import path
from .views import *



urlpatterns = [
    path('doctorcreate/', DoctorCreate.as_view(), name='doctorcreate'),
    path('doctor/<int:id>/', DoctorDetail.as_view(), name='doctordetail'),
    path('doctorlist/', ListDoctor.as_view(), name='doctorlist'),
    
    
    path('nursecreate/', NurseCreate.as_view(), name='nursecreate'),
    path('nurse/<int:id>/', NurseDetail.as_view(), name='nursedetail'),
    path('nurselist/', ListNurse.as_view(), name='nurselist'),
    
    
    # path('attenderscreate/', AttendersCreate.as_view(), name='attenderscreate'),
    # path('attenders/<int:id>/', AttendersDetail.as_view(), name='attendersdetail'),
    # path('attenderslist/', ListAttenders.as_view(), name='attenderslist'),
    
    
    # path('securitycreate/', SecurityCreate.as_view(), name='securitycreate'),
    # path('security/<int:id>/', SecurityDetail.as_view(), name='securitydetail'),
    # path('securitylist/', ListSecurity.as_view(), name='securitylist'),
    
    
    # path('receptionistcreate/', ReceptionistCreate.as_view(), name='receptionistcreate'),
    # path('receptionist/<int:id>/', ReceptionistDetail.as_view(), name='receptionistdetail'),
    # path('receptionistlist/', ListReceptionist.as_view(), name='receptionistlist'),
    
    
    # path('managerscreate/', ManagersCreate.as_view(), name='managerscreate'),
    # path('managers/<int:id>/', ManagersDetail.as_view(), name='managersdetail'),
    # path('managerslist/', ListManagers.as_view(), name='managerslist'),
    
    
    # path('labassistantcreate/', LabassistantCreate.as_view(), name='labassistantcreate'),
    # path('labassistant/<int:id>/', LabassistantDetail.as_view(), name='labassistantdetail'),
    # path('labassistantlist/', ListLabassistant.as_view(), name='labassistantlist'),
    
    
    # path('helperscreate/', HelpersCreate.as_view(), name='helperscreate'),
    # path('helpers/<int:id>/', HelpersDetail.as_view(), name='helpersdetail'),
    # path('helperslist/', ListHelpers.as_view(), name='helperslist'),
    
    
    # path('otherscreate/', OthersCreate.as_view(), name='otherscreate'),
    # path('others/<int:id>/', OthersDetail.as_view(), name='othersdetail'),
    # path('otherslist/', ListOthers.as_view(), name='otherslist'),
    
    
    # path('stafflist/', ListStaff.as_view(), name='stafflist'),
    # path('staff/<int:id>', StaffDetail.as_view(), name='staff'), 
    
    path('staffcreate/',StaffCreate.as_view(),name='staffcreate'),
    path('staffdetail/<int:id>/',StaffDetail.as_view(),name='staffdetail'),
    path('stafflist/',Stafflist.as_view(),name='stafflist'),
    
]
