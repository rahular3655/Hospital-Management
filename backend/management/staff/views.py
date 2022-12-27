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
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

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
    

# #attenders--------------------------------------------------------------------------------------------------------


# class AttendersCreate(generics.CreateAPIView):
#     queryset=Attenders.objects.all()
#     permission_classes = (AllowAny,)
#     serializer_class=AttendersSerializer

# class AttendersDetail(APIView):
#     def get_object(self,id):
#         try:
#             return Attenders.objects.get(id=id)
#         except Attenders.DoesNotExist:
#             raise status.HTTP_404_NOT_FOUND
    
#     def get (self,request,id,format=None):
#         attenders=self.get_object(id)
#         serializer=AttendersSerializer(attenders)
#         return Response(serializer.data)
        
#     def patch(self,request,id,format=None):
#         attenders=self.get_object(id)
#         serializer=AttendersSerializer(attenders,data=request.data,partial=True)
#         print(serializer)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,id,format=None):
#         attenders=self.get_object(id)
#         attenders.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

# class ListAttenders(generics.ListAPIView):
#     queryset=Attenders.objects.all()
#     serializer_class=AttendersSerializer
    
    
# #Security---------------------------------------------------

# class SecurityCreate(generics.CreateAPIView):
#     queryset=Security.objects.all()
#     permission_classes = (AllowAny,)
#     serializer_class=SecuritySerializer

# class SecurityDetail(APIView):
#     def get_object(self,id):
#         try:
#             return Security.objects.get(id=id)
#         except Security.DoesNotExist:
#             raise status.HTTP_404_NOT_FOUND
    
#     def get (self,request,id,format=None):
#         security=self.get_object(id)
#         serializer=SecuritySerializer(security)
#         return Response(serializer.data)
        
#     def patch(self,request,id,format=None):
#         security=self.get_object(id)
#         serializer=SecuritySerializer(security,data=request.data,partial=True)
#         print(serializer)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,id,format=None):
#         security=self.get_object(id)
#         security.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

# class ListSecurity(generics.ListAPIView):
#     queryset=Attenders.objects.all()
#     serializer_class=AttendersSerializer
    
# #Receptionist--------------------------------------------------------------------------


# class ReceptionistCreate(generics.CreateAPIView):
#     queryset=Receptionist.objects.all()
#     permission_classes = (AllowAny,)
#     serializer_class=ReceptionistSerializer

# class ReceptionistDetail(APIView):
#     def get_object(self,id):
#         try:
#             return Receptionist.objects.get(id=id)
#         except Receptionist.DoesNotExist:
#             raise status.HTTP_404_NOT_FOUND
    
#     def get (self,request,id,format=None):
#         receptionist=self.get_object(id)
#         serializer=ReceptionistSerializer(receptionist)
#         return Response(serializer.data)
        
#     def patch(self,request,id,format=None):
#         receptionist=self.get_object(id)
#         serializer=ReceptionistSerializer(receptionist,data=request.data,partial=True)
#         print(serializer)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,id,format=None):
#         receptionist=self.get_object(id)
#         receptionist.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

# class ListReceptionist(generics.ListAPIView):
#     queryset=Receptionist.objects.all()
#     serializer_class=ReceptionistSerializer
    
    
# #Managers------------------------------------------------------------------------------------------


# class ManagersCreate(generics.CreateAPIView):
#     queryset=   Managers.objects.all()
#     permission_classes = (AllowAny,)
#     serializer_class=   ManagersSerializer

# class ManagersDetail(APIView):
#     def get_object(self,id):
#         try:
#             return  Managers.objects.get(id=id)
#         except  Managers.DoesNotExist:
#             raise status.HTTP_404_NOT_FOUND
    
#     def get (self,request,id,format=None):
#         managers=self.get_object(id)
#         serializer= ManagersSerializer(managers)
#         return Response(serializer.data)
        
#     def patch(self,request,id,format=None):
#         managers=self.get_object(id)
#         serializer= ManagersSerializer(managers,data=request.data,partial=True)
#         print(serializer)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,id,format=None):
#         managers=self.get_object(id)
#         managers.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

# class ListManagers(generics.ListAPIView):
#     queryset=Managers.objects.all()
#     serializer_class=ManagersSerializer
    

# #Labassistant--------------------------------------------------------------------------------


# class LabassistantCreate(generics.CreateAPIView):
#     queryset=   Labassistant.objects.all()
#     permission_classes = (AllowAny,)
#     serializer_class=   LabassistantSerializer

# class LabassistantDetail(APIView):
#     def get_object(self,id):
#         try:
#             return  Labassistant.objects.get(id=id)
#         except  Labassistant.DoesNotExist:
#             raise status.HTTP_404_NOT_FOUND
    
#     def get (self,request,id,format=None):
#         labassistant=self.get_object(id)
#         serializer= LabassistantSerializer(labassistant)
#         return Response(serializer.data)
        
#     def patch(self,request,id,format=None):
#         labassistant=self.get_object(id)
#         serializer= LabassistantSerializer(labassistant,data=request.data,partial=True)
#         print(serializer)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,id,format=None):
#         labassistant=self.get_object(id)
#         labassistant.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

# class ListLabassistant(generics.ListAPIView):
#     queryset=Labassistant.objects.all()
#     serializer_class=LabassistantSerializer
    
    
# #Helpers-----------------------------------------------------------------------------------------


# class HelpersCreate(generics.CreateAPIView):
#     queryset=   Helpers.objects.all()
#     permission_classes = (AllowAny,)
#     serializer_class=   HelpersSerializer

# class HelpersDetail(APIView):
#     def get_object(self,id):
#         try:
#             return  Helpers.objects.get(id=id)
#         except  Helpers.DoesNotExist:
#             raise status.HTTP_404_NOT_FOUND
    
#     def get (self,request,id,format=None):
#         helpers=self.get_object(id)
#         serializer= HelpersSerializer(helpers)
#         return Response(serializer.data)
        
#     def patch(self,request,id,format=None):
#         helpers=self.get_object(id)
#         serializer= HelpersSerializer(helpers,data=request.data,partial=True)
#         print(serializer)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,id,format=None):
#         helpers=self.get_object(id)
#         helpers.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

# class ListHelpers(generics.ListAPIView):
#     queryset=Helpers.objects.all()
#     serializer_class=HelpersSerializer
    

# #Otheremployees--------------------------------------------------------------


# class OthersCreate(generics.CreateAPIView):
#     queryset= Others.objects.all()
#     permission_classes = (AllowAny,)
#     serializer_class=   OthersSerializer

# class OthersDetail(APIView):
#     def get_object(self,id):
#         try:
#             return Others.objects.get(id=id)
#         except Others.DoesNotExist:
#             raise status.HTTP_404_NOT_FOUND
    
#     def get (self,request,id,format=None):
#         others=self.get_object(id)
#         serializer= OthersSerializer(others)
#         return Response(serializer.data)
        
#     def patch(self,request,id,format=None):
#         others=self.get_object(id)
#         serializer= OthersSerializer(others,data=request.data,partial=True)
#         print(serializer)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,id,format=None):
#         others=self.get_object(id)
#         others.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

# class ListOthers(generics.ListAPIView):
#     queryset=Others.objects.all()
#     serializer_class=OthersSerializer
    


# #staff-----------------------------------------------------------------------

# class StaffDetail(APIView):
#     def get_object(self,id):
#         try:
#             return Staff.objects.get(id=id)
#         except Staff.DoesNotExist:
#             raise status.HTTP_404_NOT_FOUND
    
#     def get (self,request,id,format=None):
#         staffs=self.get_object(id)
#         serializer= StaffSerializer(staffs)
#         return Response(serializer.data)

# class ListStaff(generics.ListAPIView):
#     queryset=Staff.objects.all()
#     serializer_class=StaffSerializer
    
    
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
        