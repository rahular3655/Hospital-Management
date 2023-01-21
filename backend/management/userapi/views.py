from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .serializers import *
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
    


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = RegisterSerializer
    
    
class Listuser(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    
class DeleteUser(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAdminUser,IsAuthenticated)

    def delete(self, request, id):
        user = request.user
        print(user)
        if  user.is_superuser:
            snippet = User.objects.get(id=id)
            snippet.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data={'error': 'Unauthorized'})

class UpdateUser(APIView):
    def get_object(self,id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
        
    def put(self,request,id,format=None):
        user=self.get_object(id)
        serializer=UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
