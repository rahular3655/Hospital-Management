from django.urls import path
from userapi.views import *
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('listuser/', Listuser.as_view(), name='listuser'),
    path('updateuser/<int:id>/', UpdateUser.as_view(), name='updateuser'),
    
    
    
]