from django.db import models
from unidades.models.unidades_habit import Unidad_habit

# Create your models here.

class Mascota(models.Model):


    TIPO_MASC_CHOICES = (
        ('P', 'Perro'),
        ('G', 'Gato'),
    )


    id = models.AutoField(primary_key=True)
    tipo_mascota =models.CharField(max_length=4, choices=TIPO_MASC_CHOICES)
    raza = models.CharField(max_length=50)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True, null=True)
    is_delete      = models.BooleanField(default=False)
    Unidad_habit = models.ForeignKey(Unidad_habit, on_delete=models.CASCADE)