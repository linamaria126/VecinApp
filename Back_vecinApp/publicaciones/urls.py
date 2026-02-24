from rest_framework import routers
from django.urls import path, include
from .views import PublicacionViewSet

router_publicaciones = routers.DefaultRouter()
router_publicaciones.register(r'publicaciones', PublicacionViewSet, 'publicaciones')

urlpatterns = [
    path('api/', include(router_publicaciones.urls)),
]