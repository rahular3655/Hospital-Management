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
        
class patientserializer(serializers.ModelSerializer):
    class Meta:
        model=Patients 
        fields="__all__"
    
    def get_field_names(self, declared_fields,info):
        expanded_fields = super(patientserializer, self).get_field_names(declared_fields,info)
        for field in declared_fields:
            if isinstance(field, serializers.RelatedField):
                expanded_fields.append(field.queryset.model._meta.pk)
        return expanded_fields 
            
class PatientCreateSerializer(ModelSerializer):
    class Meta:
        model = Patients
        fields = "__all__"