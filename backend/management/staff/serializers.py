from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *





class DoctorSerializer(ModelSerializer):
    # doctorname=serializers.CharField(source='name')
    # doctorid=serializers.CharField(source='id')
    class Meta:
        model=Doctor
        fields= "__all__"
        
class DoctorList_Serializer(ModelSerializer):
    
    class Meta:
        model=Doctor
        fields=('id','name','specialized_in','image','phonenumber','status')
        
class NurseSerializer(ModelSerializer):
    class Meta:
        model=Nurse
        fields="__all__"
        
class StaffFormsSerializer(ModelSerializer):
    class Meta:
        model=StaffForms
        fields="__all__"
        