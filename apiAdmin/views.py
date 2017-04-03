"""
Sysadmin views
"""
from django.contrib.auth.models import User, Group

from rest_framework import permissions, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework.authentication import TokenAuthentication
from rest_auth.registration.views import LoginView

from rest_framework import serializers, viewsets

from security.permissions import IsAuthenticatedOrCreate, IsSuperUserOrAuthenticated

from apiAdmin.serializers import UserRegisterSerializer, UserSerializer, GroupSerializer


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def api_root(request, format=None):
    """API Root"""
    return Response({
        'swagger': reverse('swagger-root', request=request, format=format),
        'users': reverse('snippets-user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })


class UserRegister(generics.CreateAPIView):
    """
    Register a new user
    """
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = (IsAuthenticatedOrCreate,)


class UserViewSet(viewsets.ModelViewSet):
    """
    List or modify users
    """
    permission_classes = [IsSuperUserOrAuthenticated, ]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    List or modify groups
    """
    permission_classes = [IsSuperUserOrAuthenticated, ]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class LoginViewCustom(LoginView):
    """
    see https://github.com/Tivix/django-rest-auth/issues/159#issuecomment-173909852
    fix problem "CSRF Failed: CSRF token missing or incorrect."
    """
    authentication_classes = (TokenAuthentication,)
