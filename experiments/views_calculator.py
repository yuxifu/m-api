"""
"""
from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.conf import settings

from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes

# Create your views here.


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def add(request, numbers=None):
    """
    Add a list of comma-seperated numbers.
    """
    if numbers is not None:
        numbers = [int(x) for x in numbers.split(',') if x.strip().isdigit()]
        return HttpResponse(str(sum(numbers)), content_type="text/plain")
    else:
        return HttpResponse("calculator.add, no input",
                            content_type="text/plain")
