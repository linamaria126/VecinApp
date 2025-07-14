from django.db import models

# Create your models here.
class Documento(models.Model):

     TIPO_DCTO_CHOICES = (
        ('CC', 'Cédula ciudadanía'),
        ('CE', 'Cédula extranjería'),
        ('P', 'Pasaporte'),
        ('PT', 'Permiso de trabajo'),
        ('O', 'Otro'),
    )
     numero_dcto = models.AutoField(primary_key=True)
     tipo_dcto   = models.CharField(max_length=4, choices=TIPO_DCTO_CHOICES)



     def __str__(self):
          return self.tipo_dcto


