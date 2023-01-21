from django.urls import path
from .views import *




urlpatterns = [
    path('blockcreate/', blockCreate.as_view(), name='blockcreate'),
    path('blocklist/', BlockList.as_view(), name='blocklist'),
    path('floorcreate/', floorCreate.as_view(), name='floorcreate'),
    path('bedcreate/', BedCreate.as_view(), name='bedcreate'),
    path('floorlist/', floorList.as_view(), name='floorlist'),
    path('bedlist/', BedList.as_view(), name='bedlist'),
    path('countof/', countof.as_view(), name='countof'),
]
