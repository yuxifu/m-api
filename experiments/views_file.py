"""
"""
import os
import mimetypes
from django.shortcuts import render
from django.http import Http404, HttpResponse, StreamingHttpResponse
from django.conf import settings
from wsgiref.util import FileWrapper

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

# Create your views here.


def get_file_http_response(file, guess_type, attachment):
    STATIC_URL = getattr(settings, "STATIC_ROOT", None)
    fullpath = os.path.join(STATIC_URL, file)
    filename = os.path.basename(fullpath)
    content_type = 'application/octet-stream'
    if guess_type:
        content_type = mimetypes.guess_type(fullpath)[0]
    response = StreamingHttpResponse(FileWrapper(open(fullpath, 'rb')),
                                     content_type=content_type)
    response['Content-Length'] = os.path.getsize(fullpath)
    if attachment:
        response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def pdf(request):
    return get_file_http_response('sample.pdf', True, True)


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def zip(request):
    return get_file_http_response('sample.zip', True, True)


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def jpeg(request):
    return get_file_http_response('sample.jpeg', True, False)
