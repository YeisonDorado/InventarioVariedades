from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controladores.ControladorCliente import ControladorCliente
from Controladores.ControladorProveedor import ControladorProveedor
from Controladores.ControladorProducto import ControladorProducto


app=Flask(__name__)
"""
los cors permiten hacer pruebas al servidor desde la misma maquina en la que esta corriendo el proyecto 
"""
cors = CORS(app)

"""
Implementacion de los controladores--------------------------------
"""


miControladorCliente=ControladorCliente()
miControladorProveedor=ControladorProveedor()
miControladorProducto=ControladorProducto()

"""
implementacion de los metodos

"""

"""

----------------------------------------------SERVICIOS CLIENTES___________________________________________________________________________
"""

@app.route("/clientes",methods=['GET'])
def getClientes():
    json=miControladorCliente.index()
    return jsonify(json)
@app.route("/clientes",methods=['POST'])
def crearCliente():
    data = request.get_json()
    json=miControladorCliente.create(data)
    return jsonify(json)
@app.route("/clientes/<string:id>",methods=['GET'])
def getCliente(id):
    json=miControladorCliente.show(id)
    return jsonify(json)
@app.route("/clientes/<string:id>",methods=['PUT'])
def modificarCliente(id):
    data = request.get_json()
    json=miControladorCliente.update(id,data)
    return jsonify(json)
@app.route("/clientes/<string:id>",methods=['DELETE'])
def eliminarCliente(id):
    json=miControladorCliente.delete(id)
    return jsonify(json)



"""

----------------------------------------------SERVICIOS PRODUCTOS___________________________________________________________________________
"""

@app.route("/productos",methods=['GET'])
def getProductos():
    json=miControladorProducto.index()
    return jsonify(json)
@app.route("/productos",methods=['POST'])
def crearProducto():
    data = request.get_json()
    json=miControladorProducto.create(data)
    return jsonify(json)
@app.route("/productos/<string:id>",methods=['GET'])
def getProducto(id):
    json=miControladorProducto.show(id)
    return jsonify(json)
@app.route("/productos/<string:id>",methods=['PUT'])
def modificarProducto(id):
    data = request.get_json()
    json=miControladorProducto.update(id,data)
    return jsonify(json)
@app.route("/productos/<string:id>",methods=['DELETE'])
def eliminarProducto(id):
    json=miControladorProducto.delete(id)
    return jsonify(json)

"""
metodo de relacion provvedor - producto 
"""

@app.route("/productos/<string:id>/proveedor/<string:id_proveedor>", methods=['PUT'])
def asignarProveedorAProducto(id, id_proveedor):
    json = miControladorProducto.asignarProveedor(id, id_proveedor)
    return jsonify(json)



"""
----------------------------------------------SERVICIOS PROVEEDORES___________________________________________________________________________
"""

@app.route("/proveedores",methods=['GET'])
def getProveedores():
    json=miControladorProveedor.index()
    return jsonify(json)
@app.route("/proveedores",methods=['POST'])
def crearProveedor():
    data = request.get_json()
    json=miControladorProveedor.create(data)
    return jsonify(json)
@app.route("/proveedores/<string:id>",methods=['GET'])
def getProveedor(id):
    json=miControladorProveedor.show(id)
    return jsonify(json)
@app.route("/proveedores/<string:id>",methods=['PUT'])
def modificarProveedor(id):
    data = request.get_json()
    json=miControladorProveedor.update(id,data)
    return jsonify(json)
@app.route("/proveedores/<string:id>",methods=['DELETE'])
def eliminarProveedor(id):
    json=miControladorProveedor.delete(id)
    return jsonify(json)





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