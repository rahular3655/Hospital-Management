from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *


class DoctorSerializer(ModelSerializer):
    
    class Meta:
        model=User
        fields= "__all__"
        
class DoctorList_Serializer(ModelSerializer):
    
    class Meta:
        model=User
        fields=('id','name','specialized_in','image','phonenumber','status')
        
class NurseSerializer(ModelSerializer):
    class Meta:
        model=User
        fields="__all__"
        
class StaffFormsSerializer(ModelSerializer):
    class Meta:
        model=User
        fields="__all__"
        