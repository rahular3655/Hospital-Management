from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *



class BlockSerializer(ModelSerializer):
    class Meta:
        model=Block
        fields = "__all__"
        
class FloorSerializer(ModelSerializer):
    class Meta:
        model = Floors
        fields = "__all__"
        
class BedSerializer(ModelSerializer):
    class Meta:
        model=Bed 
        fields= "__all__"