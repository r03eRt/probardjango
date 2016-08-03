from django.shortcuts import render

# Create your views here.

# Defino la vista y digo que va a devoler un template con contexto, falta anadirla como url
def inicio(request):
    titulo = "Bienvenidos"
    # Usuario identificado
    if request.user.is_authenticated():
        titulo = "Hola, %s!" %(request.user)
    context = {
        "titulo_template": titulo
    }
    return render(request, "inicio.html", context)