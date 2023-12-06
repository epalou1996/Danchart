from django.http import HttpResponse 
from django.template import Template, Context 
from django.template import loader
from django.shortcuts import render
import datetime  

class Persona(object):

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.nombre_completo = self.nombre +' '+ self.apellido
        print(self.nombre_completo)

def saludo(request):

    programador = Persona('Eduardo', "Palou")
    hora_actual = datetime.datetime.now().hour
    minuto_actual = datetime.datetime.now().minute
    fecha_actual = datetime.datetime.now()

    ctx_saludo = {'persona': programador, 'hora_actual': (hora_actual , minuto_actual), 'fecha_actual': fecha_actual, 'lista': ["Arte","Tiktok","Viajes"]}
    return render(request, 'saludo.html', ctx_saludo)

def cuadros(request):
    fecha_actual = datetime.datetime.now()
    return render(request, 'cuadros.html', {'dame_fecha': fecha_actual})

def calculaEdad (request, agno):

    edad = 18
    periodo = agno - 2023
    edadFutura = edad + periodo

    documento =''' <html>
    <body>
    <h2>
    En el %s tendras: %s
    </h2>
    </body>
    </html>  ''' % (agno, edadFutura)
   
    return HttpResponse(documento)

