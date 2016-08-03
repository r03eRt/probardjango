from django.shortcuts import render

# Create your views here.

from .models import Registrado
from .forms import RegistradoForm

# Defino la vista y digo que va a devoler un template con contexto, falta anadirla como url
def inicio(request):
    titulo = "Bienvenidos"
    # Para guardar en base de datos ponemos post y none para evitar validadicones internas
    form = RegistradoForm(request.POST or None)
    # Usuario identificado
    #if request.user.is_authenticated():
    #    titulo = "Hola, %s!" %(request.user)
    if form.is_valid():
        # Antes de guardar haremos cosas
        #instance = form.save(commit=False)
        form.save()

    # Paso los datos como contexto a la vista
    context = {
        "titulo_template": titulo,
        # Anadidos moodel form
        "form": form
    }

    return render(request, "inicio.html", context)