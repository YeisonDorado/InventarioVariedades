from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app=Flask(__name__)
"""
los cors permiten hacer pruebas al servidor desde la misma maquina en la que esta corriendo el proyecto 
"""
cors = CORS(app)

"""
Implementacion de los controladores--------------------------------
"""







"""
implementacion de los metodos
"""
"""
----------------------------------------------SERVICIOS CLIENTES___________________________________________________________________________
"""







"""
----------------------------------------------SERVICIOS PRODUCTOS___________________________________________________________________________
"""







"""
----------------------------------------------SERVICIOS PROVEEDORES___________________________________________________________________________
"""







"""
----------------------------------------------SERVICIOS COMPROBANTE-VENTA___________________________________________________________________________
"""









"-----------------------------------------------------------------------------"
"""
Servicio que el servidor ofrecerá, y este consiste en retornar un JSON el cual
tiene un mensaje que dice que el servidor está corriendo.
"""

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)

"""
Método leer el archivo de configuración del proyecto,
retornará un diccionario el cual posee la información dentro del
JSON y se podrá acceder a los atributos necesarios.
"""
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    """
       Se crea la instancia del servidor con la url del backend y puerto especificado 
       en el archivo de configuración.
       """
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])