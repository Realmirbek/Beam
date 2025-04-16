from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users.views import UserViewSet, ProfileViewSet, ProductViewSet
from django.views.generic import TemplateView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'products', ProductViewSet)




schema_view = get_schema_view(
   openapi.Info(
      title="CRUD API",
      default_version='v1',
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('', TemplateView.as_view(template_name='index.html')),
]
