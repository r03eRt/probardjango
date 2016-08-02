from django.contrib import admin

# Register your models here.

from .models import Registrado

#Registro del modelo Registrado en la vista admin con los atributos a mostrar
class AdminRegistrado(admin.ModelAdmin):
    list_display = ["__unicode__", "nombre", "codigo_postal", "timestamp", "actualizado"]
    class Meta:
        model = Registrado

#se registra en el sitio
admin.site.register(Registrado, AdminRegistrado)
