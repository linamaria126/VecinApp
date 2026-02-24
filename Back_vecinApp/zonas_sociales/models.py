from django.db import models
from unidades.models.unidades import Unidad

# Create your models here.

class Zona_social(models.Model):
    TIPO_ZONA_CHOICES = (
        ('G', 'Gimnasio'),
        ('SS', 'Salón Social'),
        ('PS', 'Piscina'),
        ('ZB', 'Zona_BBQ'),
        ('CW', 'Zona_Coworking'),
        ('OO', 'Otro'),
        
    )

    nombre = models.CharField(max_length=100, blank=True, null=True, verbose_name='Nombre de la Zona')
    tipo_zona = models.CharField(max_length=4, choices=TIPO_ZONA_CHOICES)
    descripcion = models.TextField(blank=True, null=True)
    capacidad = models.IntegerField(blank=True, null=True)
    unidad_residencial = models.ForeignKey(Unidad, on_delete=models.CASCADE, verbose_name='Unidad Residencial', null=True, related_name='zonas_sociales')
    horario_disponible = models.CharField(max_length=100, blank=True, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True, null=True)
    is_active    = models.BooleanField(default=True)
    deleted_at  = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de eliminación')

    
    def __str__(self):
        return f"{self.nombre} - {self.unidad_residencial}"

    class Meta:
        db_table = 'zonas_sociales_zona_social'
        verbose_name = 'Zona Social'
        verbose_name_plural = 'Zonas Sociales'
        ordering = ['id']
