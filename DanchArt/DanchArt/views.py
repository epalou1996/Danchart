from django.http import HttpResponse 
from django.template import Template, Context 
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


    doc_externo = open('/root/workspace/github.com/epalou1996/Django/Danchart/DanchArt/DanchArt/plantillas/saludo.html')
    plt_saludo = Template(doc_externo.read())
    doc_externo.close()
    ctx_saludo = Context({'persona': programador, 'hora_actual': (hora_actual , minuto_actual), 'fecha_actual': fecha_actual, 'lista': ["Arte","Tiktok","Viajes"]})
    documento = plt_saludo.render(ctx_saludo)


    return HttpResponse(documento)

def despedida(request):

    doc_externo = open('/root/workspace/github.com/epalou1996/Django/Danchart/DanchArt/DanchArt/plantillas/despedida.html')
    plt_saludo = Template(doc_externo.read())
    doc_externo.close()
    ctx_saludo = Context()
    documento = plt_saludo.render(ctx_saludo)


    return HttpResponse(documento)

def dar_fecha(request):
    fecha_actual = datetime.datetime.now()

    documento = '''<html>
    <body>
    <h2>
    La hora actual es: %s
    </h2>
    </body>
    </html> ''' % fecha_actual

    return HttpResponse(documento)


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

'''

def view_creator(name_template):
    def decorator(view_func):
        def inner_func(request, filename):
            path = '/root/workspace/github.com/epalou1996/Django/Danchart/DanchArt/DanchArt/plantillas/'
            doc_externo = open(path + name_template)
            plantilla = Template(doc_externo.read())
            doc_externo.close()
            contexto = Context()
            documento = plantilla.render(contexto)

            # Utiliza la función original para obtener la respuesta y luego envuélvela en HttpResponse
            response = view_func(request, filename)
            if not isinstance(response, HttpResponse):
                # Puedes personalizar cómo manejar el resultado de la función original si es necesario
                response = HttpResponse(response)

            return response

        return inner_func

    return decorator

@view_creator(name_template="saludo.html")
def saludo_view(request, filename):
    # La lógica de tu vista original aquí
    return HttpResponse(f"Hola, mundo")

@view_creator(name_template="despedida.html")
def despedida_view(request, filename):
    # La lógica de tu vista original aquí
    return HttpResponse(f"Adios, mundo")       

'''        
        







