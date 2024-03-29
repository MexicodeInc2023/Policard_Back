from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from django.conf import settings


from apps.users.views import LoginAPIView, LogoutAPIView, RegisterView

schema_view = get_schema_view(
   openapi.Info(
      title="POLICARD API",
      default_version='v2',
      description="API para la pagina Policard",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/logout/', LogoutAPIView.as_view(), name = 'logout'),
    path('api/login/',LoginAPIView.as_view(), name = 'login'),
    path('api/register/',RegisterView.as_view(),name="register"),

    path('api/', include('apps.users.urls'), name='users'),
    
    path(r'docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
