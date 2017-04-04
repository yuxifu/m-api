from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.views.generic import RedirectView

from apiAdmin import views

# API endpoints for UserViewSet and GroupViewSet
router = SimpleRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# API endpoints
urlpatterns = [
    # url(r'^$', views.api_root),

    # API endpoints for UserViewSet and GroupViewSet
    url(r'^administration/', include(router.urls)),

    # sign up end point
    url(r'^administration/user-register/$',
        views.UserRegister.as_view(), name="register"),
    url(r'^administration/helloworld/$',
        views.api_helloworld, name="helloworld"),
    url(r'^administration/protected/$',
        views.api_helloworld_protected, name="protected"),
]
