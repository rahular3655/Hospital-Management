from rest_framework.response import Response
import json
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import *
from .models import *
from.serailizers import *



class blockCreate(generics.CreateAPIView):
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
    
class BedList(generics.ListAPIView):
    queryset=Bed.objects.all()
    serializer_class=BedSerializer
    permission_classes=(AllowAny,)
     
class MachinesCreate(generics.CreateAPIView):
    queryset=Machines.objects.all()
    serializer_class=MachinesSerializer
    permission_classes=(IsAuthenticated,)
    
class MachinesList(generics.ListAPIView):
    queryset=Machines.objects.all()
    serializer_class=MachinesSerializer
    permission_classes=(AllowAny,)
    