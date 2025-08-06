from django.db import models
from usuarios.models import User
from unidades.models import Unidad

# Create your models here.
class Reserva(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    is_delete      = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

    def __str__(self):
        return f'Reserva {self.id} - {self.unidad} por {self.user}'