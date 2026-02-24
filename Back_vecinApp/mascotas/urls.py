from rest_framework import routers
from django.urls import path, include
from .views import MascotaViewSet

router_mascotas = routers.DefaultRouter()
router_mascotas.register(r'mascotas', MascotaViewSet, 'mascotas')

urlpatterns = [
    path('api/', include(router_mascotas.urls)),
]