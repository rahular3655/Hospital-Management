from django.shortcuts import render
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from staff.models import Doctor
from staff.serializers import DoctorSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.



class doctorProfile(APIView):
    def get(self,request):
        doctor=Doctor.objects.filter(user=request.id).all()
        serializer=DoctorSerializer(doctor,many=True)
        return Response(serializer.data,status=200)
    
class doctor_patient_list(APIView): 
    def get (self,request,id):
        try:
            doctor=Doctor.objects.prefetch_related('patients').get(id=id)
            serializer=DoctorSerializer(doctor,many=True)
            return Response(serializer.data,status=200)
        except:
            return Response("Patient Doesnot exist for this doctor",status=400)