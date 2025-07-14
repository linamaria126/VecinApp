from django.db import models
from .unidades_habit import Unidad_habit
from .parqueaderos import Parqueadero


# Create your models here.
class Vehiculo(models.Model):
    placa       = models.CharField(primary_key=True, max_length=10)
    marca       = models.CharField(max_length=50, null=True, blank=True)
    color       = models.CharField(max_length=50, null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True, null=True)
    delete      = models.BooleanField(default=False)
    unidad_habit= models.ForeignKey(Unidad_habit, on_delete=models.PROTECT, null=True)
    parqueadero = models.ForeignKey(Parqueadero, on_delete=models.PROTECT, null=True)