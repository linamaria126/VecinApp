from rest_framework import viewsets
from .models import Unidad, Division, Unidad_habit
from .serializer import UnidadSerializer, DivisionSerializer, Unidad_habitSerializer

class UnidadViewSet(viewsets.ModelViewSet):
    queryset = Unidad.objects.all()
    serializer_class = UnidadSerializer

class DivisionViewSet(viewsets.ModelViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer


class Unidad_habitViewSet(viewsets.ModelViewSet):
    queryset = Unidad_habit.objects.all()
    serializer_class = Unidad_habitSerializer   