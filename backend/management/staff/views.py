from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from .paginations import *
from rest_framework.permissions import *
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from django_auto_prefetching import AutoPrefetchViewSetMixin
# Create your views here.



class DoctorCreate(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=DoctorSerializer
    print(serializer_class.data) 
    permission_classes=(AllowAny,)
        

class DoctorDetail(APIView):
    def get_object(self,id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
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
    queryset=User.objects.all()
    permission_classes=[IsAuthenticated]
    serializer_class=DoctorSerializer
          
class DoctorList(generics.ListAPIView):
    queryset=User.objects.all()
    permission_classes=(IsAuthenticated,)
    serializer_class = DoctorList_Serializer
    pagination_class = Staff_Pagination
          
#Nurse-----------------------------------------------------------------------------------------------------------


class NurseCreate(generics.CreateAPIView):
    queryset=User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class=NurseSerializer
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class NurseDetail(AutoPrefetchViewSetMixin,APIView):
    def get_object(self,id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
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
    queryset=User.objects.all()
    serializer_class=NurseSerializer
    

        