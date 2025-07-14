from django.db import models
from .unidades import Unidad
from .divisiones import Division

# Create your models here.
class Unidad_habit(models.Model):
    id              = models.IntegerField(primary_key=True)
    cant_habitantes = models.IntegerField(default=1)
    numero_unidad_habit = models.CharField(max_length=50)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True, null=True)
    delete          = models.BooleanField(default=False)
    unidad          = models.ForeignKey(Unidad, on_delete=models.PROTECT, null=True )
    division        = models.ForeignKey(Division, on_delete=models.PROTECT, null=True )


    def __str__(self):
        return self.numero_unidad_habit