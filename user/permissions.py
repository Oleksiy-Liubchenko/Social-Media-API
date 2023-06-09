from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow GET, HEAD or OPTIONS requests all users
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow PUT, PATCH or DELETE requests only owner of object
        return obj.user == request.user
