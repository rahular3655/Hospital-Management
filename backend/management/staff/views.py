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
# Create your views here.




#doctor------------------------------------------------------------------------------------------
class DoctorCreate(generics.CreateAPIView):
    queryset=Doctor.objects.all()
    permission_classes = (AllowAny,)
    serializer_class=DoctorSerializer

class DoctorDetail(APIView):
    def get_object(self,id):
        try:
            return Doctor.objects.get(id=id)
        except Doctor.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    
    def get (self,request,id,format=None):
        doctor=self.get_object(id)
        serializer=DoctorSerializer(doctor)
        return Response(serializer.data)
        
    def patch(self,request,id,format=None):
        doctor=self.get_object(id)
        serializer=DoctorSerializer(doctor,data=request.data,partial=True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id,format=None):
        doctor=self.get_object(id)
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class ListDoctor(generics.ListAPIView):
    queryset=Doctor.objects.all()
    serializer_class=DoctorSerializer
          
#Nurse-----------------------------------------------------------------------------------------------------------


class NurseCreate(generics.CreateAPIView):
    queryset=Nurse.objects.all()
    permission_classes = (AllowAny,)
    serializer_class=NurseSerializer

class NurseDetail(APIView):
    def get_object(self,id):
        try:
            return Nurse.objects.get(id=id)
        except Nurse.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    
    def get (self,request,id,format=None):
        nurse=self.get_object(id)
        serializer=NurseSerializer(nurse)
        return Response(serializer.data)
        
    def patch(self,request,id,format=None):
        nurse=self.get_object(id)
        serializer=NurseSerializer(nurse,data=request.data,partial=True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id,format=None):
        nurse=self.get_object(id)
        nurse.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class ListNurse(generics.ListAPIView):
    queryset=Nurse.objects.all()
    serializer_class=NurseSerializer
    

#attenders--------------------------------------------------------------------------------------------------------


class AttendersCreate(generics.CreateAPIView):
    queryset=Attenders.objects.all()
    permission_classes = (AllowAny,)
    serializer_class=AttendersSerializer

class AttendersDetail(APIView):
    def get_object(self,id):
        try:
            return Attenders.objects.get(id=id)
        except Attenders.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    
    def get (self,request,id,format=None):
        attenders=self.get_object(id)
        serializer=AttendersSerializer(attenders)
        return Response(serializer.data)
        
    def patch(self,request,id,format=None):
        attenders=self.get_object(id)
        serializer=AttendersSerializer(attenders,data=request.data,partial=True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id,format=None):
        attenders=self.get_object(id)
        attenders.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class ListAttenders(generics.ListAPIView):
    queryset=Attenders.objects.all()
    serializer_class=AttendersSerializer
    
    
#Security---------------------------------------------------