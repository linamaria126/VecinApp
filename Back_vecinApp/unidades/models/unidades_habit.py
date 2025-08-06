from django.db import models
from .unidades import Unidad
from .divisiones import Division

# Create your models here.
class Unidad_habit(models.Model):
    id              = models.CharField(max_length=20, 
                                       primary_key=True, 
                                       editable=False, 
                                       help_text="ID generado automáticamente como Piso+Número+Torre (ej: 401A)")
    cant_habitantes = models.IntegerField(default=1)
    piso            = models.CharField(max_length=2,
                                       help_text='Número del piso donde se encuentra la unidad habitacional (ej: 1, 2, 3)',
                                       default='0')
    numero          = models.CharField(max_length=2,
                                       help_text='Número de la unidad habitacional dentro del piso (ej: 01, 02, 03)',
                                       default='01')
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True, null=True)
    is_delete          = models.BooleanField(default=False)
    unidad          = models.ForeignKey(Unidad, on_delete=models.SET_NULL, null=True)
    division        = models.ForeignKey(Division, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            piso = self.piso if self.piso else '00'
            numero = self.numero if self.numero else '00'
            division = self.division.id if self.division else 'X'
            self.id = f"{division}-{piso}{numero}"
        super().save(*args, **kwargs)
    
    
    def __str__(self):
        return str(self.id)