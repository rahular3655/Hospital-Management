from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import *

# Create your views here.


class PatientCreate(generics.CreateAPIView):
    queryset=Patients.objects.all()
    permission_classes = (AllowAny,)
    serializer_class=PatientSerializer
    
    
class PatientList(generics.ListAPIView):
    queryset=Doctor.objects.all()
    serializer_class=PatientSerializer
    

class MedicalCondition(generics.CreateAPIView):
    queryset=MedicalConditions.objects.all()
    permission_classes = (AllowAny,)
    serializer_class=MedicalConditionSerializer
    
    
    
class AssignPatientToDoctor(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,id)
    
    
