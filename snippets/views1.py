"""
method 1: Function based views. using decorator @api_view
rest_framework_swagger: Get/Delete OK; POST/PUT doesn't show input data
controls
"""
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from security.permissions import IsOwnerOrReadOnly

# Request objects
# REST framework introduces a Request object that extends the regular
# HttpRequest, and provides more flexible request parsing.
# request.POST  # Only handles form data.  Only works for 'POST' method.
# request.data  # Handles arbitrary data.  Works for 'POST', 'PUT' and
# 'PATCH' methods.

# Response objects
# REST framework also introduces a Response object, which is a type of
# TemplateResponse that takes unrendered content and uses content negotiation
# to determine the correct content type to return to the client.
# return Response(data)  # Renders to content type as requested by the client.
# method 1


@api_view(['GET', 'POST'])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def snippet_list(request, format=None):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(context={'request': request}, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,))
def snippet_detail(request, pk, format=None):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, context={'request': request}, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
