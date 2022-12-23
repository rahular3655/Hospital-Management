from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *





class DoctorSerializer(ModelSerializer):
    class Meta:
        model=Doctor
        fields= "__all__"
        
class NurseSerializer(ModelSerializer):
    class Meta:
        model=Nurse
        fields="__all__"
        

class SecuritySerializer(ModelSerializer):
    class Meta:
        model=Security
        fields="__all__"
        
        
class AttendersSerializer(ModelSerializer):
    class Meta:
        model=Attenders
        fields="__all__"
        
class ReceptionistSerializer(ModelSerializer):
    class Meta:
        model=Receptionist
        fields="__all__"
        

class ManagersSerializer(ModelSerializer):
    class Meta:
        model=Managers
        fields="__all__"
        
class LabassistantSerializer(ModelSerializer):
    class Meta:
        model=Labassistant
        fields="__all__"
        

class HelpersSerializer(ModelSerializer):
    class Meta:
        model=Helpers
        fields="__all__"
        
class OthersSerializer(ModelSerializer):
    class Meta:
        model=Others
        fields="__all__"

class StaffSerializer(ModelSerializer):
    class Meta:
        model=Staff
        fields="__all__"