from rest_framework import routers
from django.urls import path, include
from .views import ParqueaderoViewSet

router_parqueadero = routers.DefaultRouter()
router_parqueadero.register(r'parqueaderos', ParqueaderoViewSet, 'parqueaderos')

urlpatterns = [
    path('api/', include(router_parqueadero.urls)),
]