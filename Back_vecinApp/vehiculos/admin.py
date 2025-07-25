from django.contrib import admin
from .models import Vehiculo

# Register your models here.

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'marca', 'color', 'unidad_habit', 'parqueadero', 'created_at', 'updated_at', 'delete')
    search_fields = ('placa', 'marca', 'color')
    list_filter = ('unidad_habit', 'parqueadero', 'delete')
    ordering = ('placa',)
    list_per_page = 20