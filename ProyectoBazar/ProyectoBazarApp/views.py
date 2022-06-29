from django.shortcuts import redirect, render
from .models import *
from .forms import NuevoArticulo


def inicio(request):
    articulos = Articulo.objects.all()
    contexto = {'articulos': articulos}
    return render(request,"ProyectoBazarApp/index.html",contexto)

def crear_articulo(request):    
    
    if request.method == "POST":
        
        formulario = NuevoArticulo(request.POST)
        
        if formulario.is_valid():
            
            info_articulo = formulario.cleaned_data    
        
            articulo = Articulo(producto=info_articulo["producto"], cantidad=int(info_articulo["cantidad"]), precio=float(info_articulo["precio"]))
        
            articulo.save()
        
            return redirect("inicio")
        
        else:
        
            return render(request,"ProyectoBazarApp/formulario_articulo.html",{"form":formularioVacio})
        
    else:
        
        formularioVacio = NuevoArticulo()
        
        return render(request,"ProyectoBazarApp/formulario_articulo.html",{"form":formularioVacio})

def base(request):
    
    return render(request,"ProyectoBazarApp/base.html",{})

def nosotros(request):
    info = Nosotros.objects.all()
    contexto = {'info': info}
    return render(request,"ProyectoBazarApp/nosotros.html",contexto)

def servicios(request):
    servicios = Servicios.objects.all()
    contexto = {'servicios': servicios}
    return render(request,"ProyectoBazarApp/servicios.html",contexto)