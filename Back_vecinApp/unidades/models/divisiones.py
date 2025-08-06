from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import transaction
from .unidades import Unidad


# Create your models here.
class Division(models.Model):
    id              = models.CharField(max_length=50, 
                                       primary_key=True,
                                       editable=False,
                                       help_text='Formado por: [ID Unidad]-[ID División]')
    nombre_division = models.CharField(max_length=50,
                                       default='Torre',
                                       help_text='Tipo de agrupación arquitectónica (ej: Torre, Edificio, Manzana). Mantenga consistencia en la nomenclatura para todo el conjunto residencial.')
    numero_division = models.CharField(max_length=5,
                                       default='1', 
                                       help_text='Número, letra, o clasificación de la división dentro de la unidad (ej: 1, 2, 3 ó A, B, C). Mantenga consistencia en la nomenclatura para todo el conjunto residencial.')
    cant_pisos      = models.IntegerField(null=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True, null=True)
    updated_at      = models.DateTimeField(auto_now=True, null=True)
    is_delete       = models.BooleanField(default=False)
    unidad          = models.ForeignKey(Unidad, on_delete=models.SET_NULL, null=True)


    def clean(self):
        # 1. Ejecuta validaciones básicas de Django
        super().clean()  # Valida tipos de datos, max_length, etc.

        # 2. Validaciones personalizadas
        errors = {}

        if not self.nombre_division:
            errors['nombre_division'] = _('Este campo es requerido')
        
        if not self.numero_division:
            errors['numero_division'] = _('Este campo es requerido')
        elif not self.numero_division.isalnum():
            errors['numero_division'] = _('Solo se permiten caracteres alfanuméricos')

        if self.cant_pisos is not None and self.cant_pisos < 0:
            errors['cant_pisos'] = _('No puede ser negativo')

        if self.unidad and not self.unidad.is_active:
            errors['unidad'] = _('La unidad residencial no está activa')

        # Validación de unicidad 
        if self.numero_division and self.unidad:
            queryset = Division.objects.filter(
                unidad=self.unidad,
                numero_division__iexact=self.numero_division,  # Case insensitive
                is_delete=False
            ).exclude(pk=self.pk)
            
            if queryset.exists():
                errors['numero_division'] = _('Ya existe %(nombre)s %(numero)s en esta unidad') % {
                    'nombre': self.nombre_division.lower(),
                    'numero': self.numero_division
                }

        if errors:
            raise ValidationError(errors)
        

    def save(self, *args, **kwargs):
        with transaction.atomic(): #Valida antes de  guardar
        # Generar id compuesto
            unidad_id = str(self.unidad.id) if self.unidad else '00'
            nombre_division = self.nombre_division if self.nombre_division else '00'
            numero_division = self.numero_division if self.numero_division else '00'
            
            nuevo_id = f"{unidad_id}-{nombre_division}-{numero_division}"
            
            if self.pk and self.id != nuevo_id:
                # Elimina el registro antiguo
                Division.objects.filter(pk=self.pk).delete()
                # Crea uno nuevo con el nuevo ID
                self.pk = None
                self.id = nuevo_id
                kwargs['force_insert'] = True  # Forzar creación como nuevo registro
        
            # Si es nuevo registro o el ID no cambia
            else:
                self.id = nuevo_id

        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.id}"
    
    @property
    def cant_unidades_habit(self):
        return self.unidadhabitacional_set.count()
    
    class Meta:
        db_table = 'division'
        verbose_name = 'Division'
        verbose_name_plural = 'Divisiones'
        ordering = ['id']