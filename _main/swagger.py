"""
http://marcgibbons.github.io/django-rest-swagger/schema/
"""
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.schemas import SchemaGenerator
from rest_framework.views import APIView
from rest_framework_swagger import renderers


class SwaggerSchemaView(APIView):
    permission_classes = [AllowAny]
    renderer_classes = [
        renderers.OpenAPIRenderer,
        renderers.SwaggerUIRenderer
    ]

    def get(self, request):
        generator = SchemaGenerator(title='Tutorial API')
        schema = generator.get_schema(request=request)
        # remove request=request if want to bypass the user conext
        # schema = generator.get_schema()
        return Response(schema)
