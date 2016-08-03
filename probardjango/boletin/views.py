from django.shortcuts import render

# Create your views here.

from .models import Registrado
from .forms import RegistradoForm

# Defino la vista y digo que va a devoler un template con contexto, falta anadirla como url
def inicio(request):
    titulo = "Bienvenidos"
    # Para guardar en base de datos ponemos post y none para evitar validadicones internas
    form = RegistradoForm(request.POST or None)
    # Paso los datos como contexto a la vista
    context = {
        "titulo": titulo,
        # Anadidos moodel form
        "form": form
    }
    # Usuario identificado
    #if request.user.is_authenticated():
    #    titulo = "Hola, %s!" %(request.user)

    # Is valid si esta el registro bien
    if form.is_valid():
        # Cogemos el nombre de la vista que se ha enviado
        nombre = form.cleaned_data.get("nombre")
        email = form.cleaned_data.get("email")
        # Antes de guardar haremos cosas
        form.save()
        context = {
            "titulo": "Gracias %s, ya se ha registrado" %(nombre)
        }
        if not nombre:
            context = {
                "titulo": "Gracias %s, ya se ha registrado." %(email)
            }




    return render(request, "inicio.html", context)