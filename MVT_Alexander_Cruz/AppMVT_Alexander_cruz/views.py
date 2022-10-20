from django.shortcuts import render
from .models import Familia
from django.http import HttpResponse
# Create your views here.

def familia(request, nombre, apellido, celular,cumpleagno):
    familia = Familia(nombre=nombre, apellido=apellido, celular=celular, cumpleagno=cumpleagno)
    familia.save()
    return HttpResponse (f"""
        <p>Familia: {familia.nombre} - Nombre: {familia.apellido}
         - Celular: {familia.celular} - Cumpleaños: {familia.cumpleagno}</p>
     -- Agregado con exito.""")

def lista_fam(request):
    lista= Familia.objects.all()

    return render(request,"lista_familiar.html", {"lista_familia": lista})