from database.dataSource import DataSource
# de la carpeta database del archivo dataSource importamos la clase DataSource
from database.settings import conexion
# de la carpeta database del archivo settings importamos la biblioteca conexion


# generamos una variable  va a ser la instancia de DataSource
# la cual va a obtener todos los datos para generar la conexion.

con = DataSource(
    conexion["host"],
    conexion["user"],
    conexion["password"],
    conexion["database"],
    conexion["port"],
    conexion["tipo_bd"]
)

'''
vamos a generar las consultas que me van a traer datos

'''

# ************************************************************************

# ver Datos


def verDatosModel(id=""):
    sql = '''
    
        SELECT
            id,
            nombreDispositivo,
            idmensaje,
            fechaDispositivo,
            latitud,
            longitud,
            temperatura,
            voltajeBateria,
            idevento,
            descripcionevento,
            ciclando,
            vac,
            iac,
            vdc,
            idc,
            releciclado,
            releauxiliar,
            horometrovac,
            horometrovdc,
            fechagrabacion
          

        FROM informe_dispositivo
        
    '''

    # En caso de seleccionar un dato especifico

    # este modelo lo usamos tambien para buscar un dato

    if len(id) != 0:
        sql += '''

        WHERE informe_dispositivo like {0}

        '''.format(id)

    return con.getData(sql)

# el getData trae datos


'''
Explicacion de la funcion verDatos:

al inicio nos va a traer todos los Datos y en caso
de haber un identificador nos va a traer el id a buscar.

'''


# **********************************************************************
