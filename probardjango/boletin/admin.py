from django.contrib import admin

# Register your models here.

# Anadimos el modelo formulario para poderlo tulizar
from .forms import RegistradoForm
from .models import Registrado

# Registro del modelo Registrado en la vista admin con los atributos a mostrar
class AdminRegistrado(admin.ModelAdmin):
    list_display = ["__unicode__", "nombre", "codigo_postal", "timestamp", "actualizado"]
    form = RegistradoForm
    # class Meta:
    #    model = Registrado


# Se registra en el sitio
admin.site.register(Registrado, AdminRegistrado)
