from rest_framework.response import Response
import json
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import *
from .models import *
from.serailizers import *
from.pagination import machinePagination



class blockCreate(generics.CreateAPIView):
    queryset=Block.objects.all()
    serializer_class=BlockSerializer 
    permission_classes=(AllowAny,)
    
class BlockList(generics.ListAPIView):
    queryset=Block.objects.all()
    serializer_class=BlockSerializer
    permission_classes=(AllowAny,)
    
class floorCreate(generics.CreateAPIView):
    queryset=Floors.objects.all()
    serializer_class=FloorSerializer
    permission_classes=(AllowAny,)
    
class BedCreate(generics.CreateAPIView):
    queryset = Bed.objects.all()
    serializer_class=BedSerializer
    permission_classes=(AllowAny,)
    

class floorList(generics.ListAPIView):
    queryset=Floors.objects.all()
    serializer_class=FloorSerializer
    permission_classes=(AllowAny,)
    
class flooroptionlist(generics.ListAPIView):
    queryset=Floors.objects.all()
    serializer_class=FloorOptionSerializer
    permission_classes=(AllowAny,)
    
class BedList(generics.ListAPIView):
    queryset=Bed.objects.all()
    serializer_class=BedSerializer
    permission_classes=(AllowAny,)
     
class MachinesCreate(generics.CreateAPIView):
    queryset=Machines.objects.all()
    serializer_class=MachineCreateSerializer
    permission_classes=(AllowAny,)

class DeleteMachine(APIView):
    permission_classes = (AllowAny,)

    def delete(self, request, id):
        mac = Machines.objects.get(id=id)
        mac.delete()
        return Response(status=status.HTTP_200_OK)

class MachinesList(generics.ListAPIView):
    queryset=Machines.objects.all()
    serializer_class=MachinesSerializer
    permission_classes=(AllowAny,)
    pagination_class=machinePagination
    
class countof(APIView):
    def get(self,request):
        totalbed=Bed.objects.all().count()
        availablebed=Bed.objects.filter(is_available=True).count()
        unavailable=Bed.objects.filter(is_available=False).count()
        return Response({'totalbed':totalbed,
                         'availablebed':availablebed,
                         'unavailablebed':unavailable})
        
        
        
        
    
   
        
        