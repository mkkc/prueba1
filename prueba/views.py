from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

        # super().__init__()


# 1° Vista
def saludo(request):
    #nombre = "Marcelo"
    #apellido= "Cacace"

    temas_del_curso = ["Plantillas","Modelos","Formularios","Vistas","Despliegue"]
    #temas_del_curso = []

    p1 = Persona("Marcelo", "KKC")

    fecha_actual = datetime.datetime.now()

    #doc_externo = open("C:/Users/Marcelo Cacace/Documents/Django/Proyecto1/Proyecto1/plantillas/miplantilla.html")

    #plt = Template(doc_externo.read())

    #doc_externo.close()

    doc_externo = loader.get_template('miplantilla.html')

    #ctx = Context({"nombre_persona":nombre, "apellido_persona":apellido, "momento_actual":fecha_actual})
    #ctx = Context({"persona":p1, "momento_actual":fecha_actual, "temas": temas_del_curso})

    #documento = plt.render(ctx)
    documento = doc_externo.render({"persona":p1, "momento_actual":fecha_actual, "temas": temas_del_curso})

    return HttpResponse(documento)

# 2° Vista
def despedida(request):
    return HttpResponse("Chau Marcelo, nos vemos luego... Django")

# 3° Vista
def dameFecha(request):
    fecha_actual = datetime.datetime.now()
    documento = """ 
    <html>
    <body>
    <h1>
      Fecha y hora actuales 
    </h1> 
    <h2>
    %s
    </h2>
    </body>
    </html>
    """ % fecha_actual

    return HttpResponse(documento)   

# 4° Vista
def calculaEdad(request, edad, agno):
    #edad_actual = 18
    periodo= agno - 2019
    #edad_futura = edad_actual + periodo
    edad_futura = edad + periodo
    documento = """<html><body><h2>En el año %s tendrás %s</h2></body></html>""" % (agno, edad_futura)
    return HttpResponse(documento)