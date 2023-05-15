from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import *
from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError

    
    
    
class UserSerializer(ModelSerializer):
    class Meta:
        model=Account
        fields = "__all__"
            
    def create(self, validated_data):
        obj = Account.objects.create(**validated_data)
        _password = validated_data.get("password")
        obj.set_password(_password)
        obj.save()

        return obj
        
        
