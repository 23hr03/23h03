# Importa las clases Flask, jsonify y request del módulo flask
from flask import Flask, jsonify, request
# Importa la clase CORS del módulo flask_cors
from flask_cors import CORS
# Importa la clase SQLAlchemy del módulo flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
# Importa la clase Marshmallow del módulo flask_marshmallow
from flask_marshmallow import Marshmallow

# Crea una instancia de la clase Flask con el nombre de la aplicación
app = Flask(__name__)
# Configura CORS para permitir el acceso desde el frontend al backend
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:hector2303@127.0.0.1:3306/clientes"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    gmail = db.Column(db.String(400))
    dni = db.Column(db.Integer)
    direccion = db.Column(db.String(100))
      
    def __init__(self, nombre, gmail, dni, direccion,):

        self.nombre = nombre
        self.gmail = gmail
        self.dni = dni
        self.direccion = direccion 
with app.app_context():
    db.create_all()

class UsuarioSchema(ma.Schema): 

    class Meta:
        fields = ("id", "nombre", "gmail", "dni", "direccion",)
usuario_schema = UsuarioSchema()  # Objeto para serializar/deserializar un producto
usuarios_schema = UsuarioSchema(many=True)  # Objeto para serializar/deserializar múltiples productos


@app.route("/usuario", methods=["GET"])
def get_Usuario():
    all_usuarios = Usuario.query.all()  # Obtiene todos los registros de la tabla de productos
    result = usuarios_schema.dump(all_usuarios)  # Serializa los registros en formato JSON
    return jsonify(result)  # Retorna el JSON de todos los registros de la tabla
#================================================================================================
@app.route("/usuario/<id>", methods=["GET"])
def get_producto(id):
    """
    Endpoint para obtener un producto específico de la base de datos.

    Retorna un JSON con la información del producto correspondiente al ID proporcionado.
    """
    usuario = Usuario.query.get(id)  # Obtiene el producto correspondiente al ID recibido
    return usuario_schema.jsonify(usuario)  # Retorna el JSON del producto
#================================================================================================
@app.route("/usuario/<id>", methods=["DELETE"])
def delete_usuario(id):
    """
    Endpoint para eliminar un producto de la base de datos.

    Elimina el producto correspondiente al ID proporcionado y retorna un JSON con el registro eliminado.
    """
    usuario = Usuario.query.get(id)  # Obtiene el producto correspondiente al ID recibido
    db.session.delete(usuario)  # Elimina el producto de la sesión de la base de datos
    db.session.commit()  # Guarda los cambios en la base de datos
    return usuario_schema.jsonify(usuario)  # Retorna el JSON del producto eliminado
#================================================================================================
@app.route("/usuario", methods=["POST"])  # Endpoint para crear un producto
def create_usuario():
    """
    Endpoint para crear un nuevo producto en la base de datos.

    Lee los datos proporcionados en formato JSON por el cliente y crea un nuevo registro de producto en la base de datos.
    Retorna un JSON con el nuevo producto creado.
    """
    nombre = request.json["nombre"]  # Obtiene el nombre del producto del JSON proporcionado
    gmail = request.json["gmail"]  # Obtiene el precio del producto del JSON proporcionado
    dni = request.json["dni"]  # Obtiene el stock del producto del JSON proporcionado
    direccion = request.json["direccion"]  # Obtiene la imagen del producto del JSON proporcionado
   
    new_usuario = Usuario(nombre, gmail, dni, direccion)  # Crea un nuevo objeto Producto con los datos proporcionados
    db.session.add(new_usuario)  # Agrega el nuevo producto a la sesión de la base de datos
    db.session.commit()  # Guarda los cambios en la base de datos
    return usuario_schema.jsonify(new_usuario)  # Retorna el JSON del nuevo producto creado


#================================================================================================

@app.route("/usuario/<id>", methods=["PUT"])  # Endpoint para actualizar un producto
def update_producto(id):
    """
    Endpoint para actualizar un producto existente en la base de datos.

    Lee los datos proporcionados en formato JSON por el cliente y actualiza el registro del producto con el ID especificado.
    Retorna un JSON con el producto actualizado.
    """
    usuario = Usuario.query.get(id)  # Obtiene el producto existente con el ID especificado

    # Actualiza los atributos del producto con los datos proporcionados en el JSON
    usuario.nombre = request.json["nombre"]
    usuario.gmail = request.json["gmail"]
    usuario.dni = request.json["dni"]
    usuario.diereccion = request.json["direccion"]
    

    db.session.commit()  # Guarda los cambios en la base de datos
    return usuario_schema.jsonify(usuario)  # Retorna el JSON del producto actualizado


#================================================================================================
# Programa Principal
if __name__ == "__main__":
    # Ejecuta el servidor Flask en el puerto 5000 en modo de depuración
    app.run(debug=True, port=5001)