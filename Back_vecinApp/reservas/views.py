from rest_framework import viewsets
from .models import Reserva
from .serializer import ReservaSerializer

# Create your views here.
class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer