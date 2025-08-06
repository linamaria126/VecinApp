from django.db import models
from unidades.models import Unidad_habit
from parqueaderos.models import Parqueadero



# Create your models here.
class Vehiculo(models.Model):
    placa       = models.CharField(primary_key=True, max_length=10)
    marca       = models.CharField(max_length=50, null=True, blank=True)
    color       = models.CharField(max_length=50, null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True, null=True)
    is_delete      = models.BooleanField(default=False)
    unidad_habit= models.ForeignKey(Unidad_habit, on_delete=models.SET_NULL, null=True)
    parqueadero = models.ForeignKey(Parqueadero, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.placa
    
    class Meta:
        db_table = 'vehiculo'
        verbose_name = 'Vehículo'
        verbose_name_plural = 'Vehículos'
        ordering = ['placa']
        unique_together = ('placa', 'unidad_habit')    
    