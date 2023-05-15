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
from staff.models import *
from infrastructure.models import *
from .pagination import *
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.


class PatientCreate(generics.CreateAPIView):
    queryset=Patients.objects.all()
    permission_classes = (AllowAny,)
    serializer_class=PatientCreateSerializer
    
class DeletePatient(APIView):
    authentication_classes=(JWTAuthentication,)
    permission_classes = (AllowAny,)

    def delete(self, request, id):
        patient = Patients.objects.get(id=id)
        patient.delete()
        return Response(status=status.HTTP_200_OK)
        
    
    
class PatientList(generics.ListAPIView):
    queryset=Patients.objects.all()
    permission_classes=(AllowAny,)
    serializer_class=PatientSerializer
    pagination_class=PatientPagination
    
    

class MedicalCondition(generics.CreateAPIView):
    queryset=MedicalConditions.objects.all()
    permission_classes = (AllowAny,)
    serializer_class=MedicalConditionSerializer
    
    
    
class AssignPatientToDoctor(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        patid=request.data["patid"]
        docid=request.data["docid"]
        doc=Doctor.objects.get(id=docid)
        pat=Patients.objects.get(id=patid)
        pat.doctor=doc
        pat.save()
        return Response(status=status.HTTP_200_OK)
    
    
class AdmitPatient(APIView):
    # permission_classes=[IsAuthenticated]
    def post(self,request):
        print(request.data)
        patid=request.data["patid"]
        bedid=request.data["bedid"]
        patient=Patients.objects.get(id=patid)
        patient.status="Admitted"
        patient.alloted=True
        bed=Bed.objects.get(id=bedid)
        bed.reserved_by=patient 
        bed.is_available=False
        bed.save()
        patient.save()
        return Response(status=status.HTTP_200_OK)


    
