from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *
from staff.serializers import *
from .serializers import *
from infrastructure.serailizers import *




        
class MedicalConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model=MedicalConditions
        fields="__all__"
        
class PatientSerializer(serializers.ModelSerializer):
    doctors=DoctorSerializer(many=True)
    medical_condition=MedicalConditionSerializer(many=True,read_only=True)
    patientbed=BedSerializer(many=True,read_only=True)
    class Meta:
        model= Patients
        fields= "__all__"
        

            
class PatientCreateSerializer(ModelSerializer):
    class Meta:
        model = Patients
        fields = "__all__"