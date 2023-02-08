# importamos todos los modelos
# con el * importa todos los modelos
from models.models import *

# vamos a utilizar una libreria de flask que es el jsonify para
# convertir directamente a formato json cada uno de los parametros.
# para posteriormente en las funciones de ver y demas este en
# formato json.

from flask import jsonify


# ********************************************************************
# ver Datos

def verDatosController(id=""):

    # vamos a obtener los datos
    # y los obtenemos sobre la consulta que nos negera el modelo.

    # ejecutamos el modelo y le agregarmos el id
    # si no hay id para filtrar nos hara una consulta de SELECT normal.
    datos = verDatosModel(id)

    # una vez obteniendo los datos haremos una estructura json

    result = []

    # estructura formato json
    # nos trae una lista, una vez traida la lista hay que recorrer
    # fila por fila usaremos un ciclo for

    for row in datos:
        contenido = {
            'id': row[0],
            'nombreDispositivo': row[1],
            'idmensaje': row[2],
            'fechaDispositivo': row[3],
            'latitud': row[4],
            'longitud': row[5],
            'temperatura': row[6],
            'voltajeBateria': row[7],
            'idevento': row[8],
            'descripcionevento': row[9],
            'ciclando': row[10],
            'vac': row[11],
            'iac': row[12],
            'vdc': row[13],
            'idc': row[14],
            'releciclado': row[15],
            'releauxiliar': row[16],
            'horometrovac': row[17],
            'horometrovdc': row[18],
            'fechagrabacion': row[19]
        }
        result.append(contenido)
        # con el append la agregamos a la lista de arriba result
        # en esta lista estara todos los datos que tecnicamente
        # traiga la consulta

    return jsonify(result)  # usamos jsonify para convertirlo a formato json


# **********************************************************************
