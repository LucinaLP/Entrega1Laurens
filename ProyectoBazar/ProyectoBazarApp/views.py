from django.shortcuts import render
from .models import *


def index(request):
    articulos = Articulo.objects.all()
    contexto = {'articulos': articulos}
    return render(request,"ProyectoBazarApp/index.html",contexto)

def nosotros(request):
    info = Nosotros.objects.all()
    contexto = {'info': info}
    return render(request,"ProyectoBazarApp/nosotros.html",contexto)

def servicios(request):
    servicios = Servicios.objects.all()
    contexto = {'servicios': servicios}
    return render(request,"ProyectoBazarApp/servicios.html",contexto)