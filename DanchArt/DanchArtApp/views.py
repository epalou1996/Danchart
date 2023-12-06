from django.http import HttpResponse 
from django.template import Template, Context 
from django.template import loader
from django.shortcuts import render
import datetime  


def home(request):
    fecha_actual = datetime.datetime.now()
    return render(request, 'DanchArtApp/home.html')

def shop(request):
    fecha_actual = datetime.datetime.now()
    return render(request, 'DanchArtApp/home.html')

