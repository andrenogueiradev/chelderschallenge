from django.contrib import admin
from django.urls import path, include
from django.urls.conf import re_path
from rest_framework.authentication import BaseAuthentication
from rest_framework.routers import DefaultRouter
from accounts.views import ClientViewSet, CompanyViewSet, UserViewSet, ManagerViewSet, LoginViewSet


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()
router.register(r'client', ClientViewSet, basename='client')
router.register(r'company', CompanyViewSet, basename='company')
router.register(r'user', UserViewSet, basename='user')
router.register(r'manager', ManagerViewSet, basename='manager')
router.register(r'login', LoginViewSet, basename='login')


schema_view = get_schema_view(
   openapi.Info(
      title="API Documentation",
      default_version='v1',
      description="Chelder's Challenge",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    re_path(r'^v1/admin/', admin.site.urls),
    re_path(r'^v1/api-auth/', include('rest_framework.urls', namespace='v1')),
    re_path(r'^v1/', include(router.urls)),
    re_path(r'^v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name = 'schema-swagger-ui'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
