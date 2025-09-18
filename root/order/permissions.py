from rest_framework.permissions import BasePermission

class GetOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method == "GET"