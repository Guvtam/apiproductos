from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Permite solicitudes de solo lectura para todos los usuarios
        if request.method in permissions.SAFE_METHODS:
            return True

        # Permite solicitudes de creación y eliminación solo para usuarios administradores
        return request.user and request.user.is_authenticated and request.user.is_superuser
