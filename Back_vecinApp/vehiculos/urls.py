from rest_framework import routers
from django.urls import path, include
from .views import VehiculoViewSet

router_vehiculos = routers.DefaultRouter()
router_vehiculos.register(r'vehiculos', VehiculoViewSet, 'vehiculos')

urlpatterns = [
    path('api/', include(router_vehiculos.urls)),
]