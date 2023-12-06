from django.http import HttpResponse 
from django.template import Template, Context 
from django.template import loader
from django.shortcuts import render
import datetime  

path = '/root/workspace/github.com/epalou1996/Django/Danchart/DanchArt/DanchArtApp/plantillas/'

def home(request):
    fecha_actual = datetime.datetime.now()
    return render(request, path+'home.html', {'dame_fecha': fecha_actual})

def shop(request):
    fecha_actual = datetime.datetime.now()
    return render(request, path+'shop.html', {'dame_fecha': fecha_actual})

