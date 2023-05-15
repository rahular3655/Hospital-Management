from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *



class BedSerializer(ModelSerializer):
    class Meta:
        model=Bed
        fields= "__all__"
        
class FloorSerializer(ModelSerializer):
    bed=BedSerializer(many=True)
    class Meta:
        model = Floors
        fields = "__all__"
        
class FloorOptionSerializer(ModelSerializer):
    label =serializers.CharField(source='name')
    value=serializers.CharField(source='id')
    class Meta:
        model = Floors
        fields = ['value','label']

class MachinesSerializer(ModelSerializer):
    class Meta:
        model=Machines
        fields="__all__"
        depth=2

class MachineCreateSerializer(ModelSerializer):
    class Meta:
        model=Machines
        fields="__all__"
        
class BlockSerializer(ModelSerializer):
    floor=FloorSerializer(many=True)
    
    class Meta:
        model=Block
        fields = "__all__"
        depth=2