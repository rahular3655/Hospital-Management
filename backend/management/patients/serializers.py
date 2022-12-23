from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *



class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model= Patients
        fields= "__all__"
        
class MedicalConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model=MedicalConditions
        fields="__all__"
        

            