from django.db import models
from .unidades_habit import Unidad_habit


# Create your models here.
class Parqueadero(models.Model):
    numero = models.IntegerField(primary_key=True)
    unidad_habit= models.ForeignKey(Unidad_habit, on_delete=models.PROTECT, null=True)
