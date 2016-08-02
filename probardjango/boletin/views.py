from django.shortcuts import render

# Create your views here.

# Defino la vista y digo que va a devoler un template con contexto, falta anadirla como url
def inicio(request):
    return render(request, "inicio.html", {})