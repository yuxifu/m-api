from rest_framework import permissions
from rest_framework.compat import is_authenticated
from rest_framework.authentication import SessionAuthentication


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user


class IsSuperUserOrAuthenticated(permissions.BasePermission):
    """
    Custom permission to only allow super user to edit and allow regular user to read
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to authenticated user
        if request.method in permissions.SAFE_METHODS:
            return request.user and is_authenticated(request.user)

        # Write permissions are only allowed to super user.
        return request.user and request.user.is_staff


class IsAuthenticatedOrCreate(permissions.IsAuthenticated):
    """
    Custom permission to allow either IsAuthenticated or Create (POST).
    """

    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return super(IsAuthenticatedOrCreate, self).has_permission(request, view)


class EverybodyCanAuthentication(SessionAuthentication):

    def authenticate(self, request):
        return None
