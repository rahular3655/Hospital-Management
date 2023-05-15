from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .serializers import *
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import *

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        print(token)
        # Add custom claims
        token['username'] = user.username
        token['role'] = user.role
        token['phone_number'] = user.phone_number
        token['is_staff'] = user.is_staff
        # ...

        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes=(AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
    

class RegisterView(generics.CreateAPIView):
    queryset = Account.objects.all()
    # permission_classes = (IsAdminUser,)
    serializer_class = UserSerializer
    # def perform_create(self,serializer):
    #     username = serializer.validated_data.get('username')
    #     password=serializer.validated_data.get("password")
    #     user=Account.objects.create(username=username)
    #     user.set_password(password)
    #     user.save()
    #     serializer.save(Account=user)

class StaffLogin(APIView,TokenObtainPairSerializer):
    def post(self, request):
        # print(request)
        # body = request.body.decode("utf-8")
        # print(body)
        # body = json.loads(body)
        data=request.data 
        print(data)
        user=authenticate(username=data['username'],password=data['password'])
        print(user,"is user")
        if user is None:
            print("NO user............")
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        elif not user.role=="FRONT-DESK":
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        if user.role=="FRONT-DESK":
            token=self.get(user)
            data={
                'refresh':str(token),
                'access':str(token.access_token)
            }
        return Response(data=data, status=status.HTTP_200_OK)

    def get_token(self, user):
        token = super().get_token(user)
        token['username']=user.username
        token['role']=user.role
        print(token.access_token)
        return token

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return self.get_token(refresh)
    
class Listuser(generics.ListAPIView):
    queryset=Account.objects.all()
    serializer_class=UserSerializer
    
class DeleteUser(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAdminUser,IsAuthenticated)

    def delete(self, request, id):
        user = request.user
        print(user)
        if  user.is_superuser:
            snippet = Account.objects.get(id=id)
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
