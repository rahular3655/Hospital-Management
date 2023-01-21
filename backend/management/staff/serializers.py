from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *





class DoctorSerializer(ModelSerializer):
    # doctorname=serializers.CharField(source='name')
    # doctorid=serializers.CharField(source='id')
    class Meta:
        model=Doctor
        fields= "__all__"
        
class NurseSerializer(ModelSerializer):
    class Meta:
        model=Nurse
        fields="__all__"
        
class StaffFormsSerializer(ModelSerializer):
    class Meta:
        model=StaffForms
        fields="__all__"
        