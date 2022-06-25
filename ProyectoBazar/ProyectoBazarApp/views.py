from django.shortcuts import render
from .models import *


def index(request):
    articulos = Articulo.objects.all()
    contexto = {'articulos': articulos}
    return render(request,"ProyectoBazarApp/index.html")

def nosotros(request):
    info = Nosotros.objects.all()
    contexto = {'info': info}
    return render(request,"ProyectoBazarApp/index.html")

def servicios(request):
    servicio = Servicios.objects.all()
    contexto = {'servicios': servicios}
    return render(request,"ProyectoBazarApp/index.html")