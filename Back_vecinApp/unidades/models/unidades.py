from django.db import models


# Create your models here.
class Unidad(models.Model):
   
    UNIDAD_HABITACIONAL_CHOICES = (
        ('A', 'Apartamento'),
        ('C', 'Casa'),
    )
    
    id         = models.AutoField(primary_key=True)
    nombre     = models.CharField(max_length=100)
    nit        = models.CharField(max_length=45)
    direccion  = models.CharField(max_length=200)
    telefono   = models.CharField(max_length=45)
    tipo_unidad_habit   = models.CharField(max_length=4, choices=UNIDAD_HABITACIONAL_CHOICES)
    cantidad_unid_habit = models.IntegerField(blank=bool(True), null=True)
    link_registro       = models.CharField(max_length=200)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True, null=True)
    delete      = models.BooleanField(default=False)

    
    # class Meta:
    #     managed = False
    #     db_table = 'Unidad_Residencial'

    def __str__(self):
        return self.nombre