from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *



class BlockSerializer(ModelSerializer):
    class Meta:
        model=Block
        fields = "__all__"
        
class FloorSerializer(ModelSerializer):
    blockname=BlockSerializer()
    class Meta:
        model = Floors
        fields = "__all__"
        
class BedSerializer(ModelSerializer):
    floor=FloorSerializer()
    class Meta:
        model=Bed 
        fields= "__all__"

class MachinesSerializer(ModelSerializer):
    floor=FloorSerializer()
    class Meta:
        model=Machines
        fields="__all__"