from rest_framework import permissions


class HasStaffPermission(permissions.BasePermission):
    """
    Permission checks if api is allowed for user.
    """

    def has_permission(self, request, view):
        return request.user.is_staff
