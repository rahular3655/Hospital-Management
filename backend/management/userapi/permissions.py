"""Module for Making custom Permissions"""
from rest_framework.permissions import BasePermission 



class IsSuperuser(BasePermission):
    def has_permission(self, request, view):
        try :
            user=request.user.is_superuser
        except AttributeError:
            return False  
        return user
    
class IsDesk(BasePermission):
    def has_permission(self, request, view):
        try:
            user=request.user.role=="FRONT-DESK"
        except AttributeError:
            return False
        return user
    
class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        try:
            user=request.user.role=="DOCTOR"
        except AttributeError:
            return False
        return user