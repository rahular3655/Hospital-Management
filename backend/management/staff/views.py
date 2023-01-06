from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from rest_framework.permissions import *
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
# Create your views here.




#doctor------------------------------------------------------------------------------------------
# class DoctorCreate(APIView):
    
#     queryset=Doctor.objects.all()
#     permission_classes = []
#     serializer_class=DoctorSerializer
#     print()
#     def perform_create(self, serializer):
#         user = self.request.user
#         print(self.request.user)
#         serializer.save(created_by=user)

class DoctorCreate(APIView):
    def post(self,request,*args,**kwargs):
        header_value=request.headers.get("Authorization")
        print(header_value,"header value..........................")
        new=DoctorSerializer(data=request.data)
        print(request.data)
        print(new)
        if new.is_valid():
            new.save()
            return Response(new.data,status=200)
        else:
            data=new.errors
            return Response(status=status.HTTP_404_NOT_FOUND)
        

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
    permission_classes=[IsAdminUser]
    serializer_class=DoctorSerializer
          
#Nurse-----------------------------------------------------------------------------------------------------------


class NurseCreate(generics.CreateAPIView):
    queryset=Nurse.objects.all()
    permission_classes = (AllowAny,)
    serializer_class=NurseSerializer
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

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
    


    
    
#staffform-------------------------------------------------

class StaffCreate(generics.CreateAPIView):
    queryset=StaffForms.objects.all()
    serializer_class = StaffFormsSerializer
    permission_classes=(AllowAny,)
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
class Stafflist(generics.ListAPIView):
    queryset=StaffForms.objects.all()
    serializer_class=StaffFormsSerializer
    
class StaffDetail(APIView):
    
    def get_object(self,id):
        try:
            return StaffForms.objects.get(id=id)
        except StaffForms.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
        
    def get(self,request,id,format=None):
        new=self.get_object(id)
        serializer=StaffFormsSerializer(new)
        return Response(serializer.data)
    
    def patch(self,request,id,format=None):
        update=self.get_object(id)
        serializer=StaffFormsSerializer(update,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id,format=None):
        tbdele=self.get_object(id)
        tbdele.delete
        return Response(status=status.HTTP_204_NO_CONTENT)
        