from django.db import models

# Create your models here.
class Division(models.Model):
    id              = models.IntegerField(primary_key=True)
    nombre_division = models.CharField(max_length=50)
    cant_unidades_habit = models.SmallIntegerField(blank=True, null=True)
    cant_pisos      = models.IntegerField(null=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True, null=True)
    delete          = models.BooleanField(default=False)


    def __str__(self):
        return self.nombre_division