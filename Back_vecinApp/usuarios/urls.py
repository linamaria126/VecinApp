from rest_framework import routers
from django.urls import path, include
from .views import UserViewSet

router_usuarios = routers.DefaultRouter()
router_usuarios.register(r'usuarios', UserViewSet, 'usuarios')

urlpatterns = [
    path('api/', include(router_usuarios.urls)),
]