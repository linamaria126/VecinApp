from rest_framework import viewsets
from .models import Zona_social
from .serializer import ZonaSocialSerializer

# Create your views here.
class ZonaSocialViewSet(viewsets.ModelViewSet):
    queryset = Zona_social.objects.all()
    serializer_class = ZonaSocialSerializer
