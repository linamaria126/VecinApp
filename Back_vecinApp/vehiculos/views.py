from rest_framework import viewsets
from .models import Vehiculo
from .serializer import VehiculoSerializer

# Create your views here.
class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
