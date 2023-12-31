from django.http import HttpResponse 
from django.template import Template, Context 
from django.template import loader
from django.shortcuts import render
import datetime  
from DanchArtApp.models import Cuadro

def home(request):
    fecha_actual = datetime.datetime.now()
    return render(request, 'DanchArtApp/home3.html')

def shop(request):
    categorias = list(Cuadro.objects.values_list('tipo', flat=True).distinct())
    tipos = []
    for cat in categorias:
        if cat != 00000:
            cuadro = Cuadro.objects.filter(tipo=cat).first()
            tipos.append(cuadro.cuadro)
    fecha_actual = datetime.datetime.now()
    zipped = zip(tipos,categorias)
    lista = list(zipped)
    lista_agrupada = [lista[i:i+3] for i in range(0, len(tipos), 3)]
    return render(request, 'DanchArtApp/shop.html', {'lista': lista_agrupada})

def galeria(request):
    categorias = list(Cuadro.objects.values_list('tipo', flat=True).distinct())
    tipos = []
    for cat in categorias:
        if cat != 00000:
            cuadro = Cuadro.objects.filter(tipo=cat).first()
            tipos.append(cuadro.cuadro)
    fecha_actual = datetime.datetime.now()
    zipped = zip(tipos,categorias)
    lista = list(zipped)
    lista_agrupada = [lista[i:i+3] for i in range(0, len(tipos), 3)]
    return render(request, 'DanchArtApp/galeria.html', {'lista': lista_agrupada})

def faq(request):
    fecha_actual = datetime.datetime.now()
    return render(request, 'DanchArtApp/faq.html')

def proceso(request):
    fecha_actual = datetime.datetime.now()
    return render(request, 'DanchArtApp/proceso.html')

def theartist(request):
    fecha_actual = datetime.datetime.now()
    return render(request, 'DanchArtApp/theartist.html')

def test1(request):
    fecha_actual = datetime.datetime.now()
    return render(request, 'DanchArtApp/test1.html')

def test2(request):
    fecha_actual = datetime.datetime.now()
    return render(request, 'DanchArtApp/test2.html')
