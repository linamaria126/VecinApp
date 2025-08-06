from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models.unidades import Unidad
from .models.divisiones import Division
from .models.unidades_habit import Unidad_habit




admin.site.register(Unidad)

admin.site.register(Unidad_habit)

@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Esto evita que el admin cree duplicados
        obj.save()





# Register your models here.
class UserAdmin(BaseUserAdmin):
    pass



