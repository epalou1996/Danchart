from django.http import HttpResponse 
from django.template import Template, Context 
from django.template import loader
from django.shortcuts import render
import datetime  


def home(request):
    fecha_actual = datetime.datetime.now()
    return render(request, 'DanchArtApp/home3.html')

def shop(request):
    fecha_actual = datetime.datetime.now()
    return render(request, 'DanchArtApp/shop.html')

def galeria(request):
    fecha_actual = datetime.datetime.now()
    return render(request, 'DanchArtApp/gallery.html')

def faq(request):
    fecha_actual = datetime.datetime.now()
    return render(request, 'DanchArtApp/faq.html')

def proceso(request):
    fecha_actual = datetime.datetime.now()
    return render(request, 'DanchArtApp/proceso.html')

def theartist(request):
    fecha_actual = datetime.datetime.now()
    return render(request, 'DanchArtApp/theartist.html')

