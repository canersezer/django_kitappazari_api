from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        is_admin = super().has_permission(request,view)
        return request.method in SAFE_METHODS or is_admin
        