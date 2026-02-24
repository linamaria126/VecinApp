from django.urls import path, include
from rest_framework import routers
from .views import UnidadViewSet, DivisionViewSet, Unidad_habitViewSet

router_unidades = routers.DefaultRouter()
router_unidades.register(r'unidades', UnidadViewSet, 'unidades')
router_unidades.register(r'divisiones', DivisionViewSet, 'divisiones')
router_unidades.register(r'unidades_habit', Unidad_habitViewSet, 'unidades_habit')


urlpatterns = [
    path('api/', include(router_unidades.urls)),
]


