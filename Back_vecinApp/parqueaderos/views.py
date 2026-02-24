from rest_framework import viewsets
from .models import Parqueadero
from .serializer import ParqueaderoSerializer

# Create your views here.
class ParqueaderoViewSet(viewsets.ModelViewSet):
    queryset = Parqueadero.objects.all()
    serializer_class = ParqueaderoSerializer
