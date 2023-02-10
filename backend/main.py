# importamos las librerias

from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin

from controllers.controller import *


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-type'


# crear las rutas permitidas para que la aplicacion empiece a funcionar

# rutas

# ********************************************************************
# ver Datos


@app.route('/InfoTelemetria')
@cross_origin()
def getALLdatos():

    return verDatosController()


# *************************************************************

# ver consulta de datos

@app.route('/InfoTelemetria/<id>')
@cross_origin()
def getdatos(id):

    return verDatosController(id)


# **************************************************************
# pagina por defecto

@app.route('/')
@cross_origin()
def index():

    return 'Servidor Telemetria'


# ************************************************************


if __name__ == '__main__':
    app.run(port=3000, debug=True)
