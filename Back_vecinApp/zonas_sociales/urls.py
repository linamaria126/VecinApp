from rest_framework import routers
from django.urls import path, include
from .views import ZonaSocialViewSet

router_zonas_sociales = routers.DefaultRouter()
router_zonas_sociales.register(r'zonas_sociales', ZonaSocialViewSet, 'zonas_sociales')


urlpatterns = [
    path('api/', include(router_zonas_sociales.urls)),
]