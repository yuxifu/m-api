"""
"""
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions

from experiments.models import SimpleEmailMessssage
from experiments.serializers import SimpleEmailMessssageSerializer


class SendSimpleEmailMessssage(mixins.ListModelMixin,
                               mixins.CreateModelMixin,
                               generics.GenericAPIView):
    """
    Send an email message
    """
    serializer_class = SimpleEmailMessssageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
