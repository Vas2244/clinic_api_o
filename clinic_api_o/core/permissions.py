from rest_framework import permissions


class IsDoctor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Doctor').exists()

class IsNurse(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Nurse').exists()

class IsDoctorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.groups.filter(name='Doctor').exists()