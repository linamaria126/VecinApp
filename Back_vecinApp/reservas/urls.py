from rest_framework import routers
from django.urls import path, include
from .views import ReservaViewSet

router_reservas = routers.DefaultRouter()
router_reservas.register(r'reservas', ReservaViewSet, 'reservas')

urlpatterns = [
    path('api/', include(router_reservas.urls)),
]