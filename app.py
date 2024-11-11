##from flask import Flask, jsonify, request
##import mariadb
##
##
##app = Flask(__name__)
##
##@app.route('/users')
##def users():
##    db = mariadb.connect(
##        user="agathaessence",
##        password="agathaessence111",
##        host="10.9.120.5",
##        database="agathaessence"
##    )
##    cur = db.cursor()
##    cur.execute("SELECT * FROM Users")
##
##    users = [column[0] for column in cur.description]
##    tabla = []
##    for row in cur:
##        tabla.append(dict(zip(users, row)))
##    
##    return jsonify(tabla)
##
##@app.route("/users/<int:id>")
##def detalle_users(id):
##    db = mariadb.connect(
##        user="agathaessence",
##        password="agathaessence111",
##        host="10.9.120.5",
##        database="agathaessence"
##    )
##    cur = db.cursor()
##    cur.execute("SELECT first_name, last_name FROM Users WHERE id_users = ?", (id,))
##    users = [column[0] for column in cur.description]
##    tabla = [dict(zip(users, row))for row in cur.fetchall()]
##    return jsonify(tabla)

from flask import Flask, jsonify, request
from flask_cors import CORS
import mariadb

app = Flask(__name__)
CORS(app)

# Muestra todos los productos
@app.route("/products")
def Productos():
    db = mariadb.connect(
        user="agathaessence",
        password="agathaessence111",
        host="10.9.120.5",
        database="agathaessence"
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM products")

    color = [column[0] for column in cur.description]
    
    tabla = []
    for row in cur:
        tabla.append(dict(zip(color, row)))

    return jsonify(tabla)

# Selecciona un producto y permite borrar
@app.route("/products/<int:id>", methods=('GET', 'DELETE'))
def borrarProducto(id):
    db = mariadb.connect(
        user="agathaessence",
        password="agathaessence111",
        host="10.9.120.5",
        database="agathaessence"
    )
    cur = db.cursor()
    sentSql1 = """SELECT * FROM Products WHERE id = ?"""
    cur.execute(sentSql1, (id,))
    producto = [column[0] for column in cur.description]
    producto_data = cur.fetchall()

    if not producto_data:
        return jsonify({"error": "Producto no encontrado"}), 404

    curC = db.cursor()
    sentSql2 = """SELECT * FROM size WHERE ID= ?"""
    curC.execute(sentSql2, (id,))
    size = [column[0] for column in curC.description]
    size_data = curC.fetchall()

    tabla = [dict(zip(producto, row)) for row in producto_data]
    tablaSize = [dict(zip(size, row)) for row in size_data]

    if request.method == 'DELETE':
        qborrar = """DELETE FROM products WHERE ID=?"""
        cur.execute(qborrar, (id,))
        db.commit()
        return jsonify({"message": "Producto borrado exitosamente"}), 200
    
    return jsonify(tabla, tablaSize)

# Permite crear un nuevo producto
@app.route("/products", methods=['POST'])
def crearProducto():
    try:
        db = mariadb.connect(
        user="agathaessence",
        password="agathaessence111",
        host="10.9.120.5",
        database="agathaessence"
        )
        cur = db.cursor()
        
        # Obtén los datos del cuerpo de la solicitud
        data = request.json
        name = data.get('name_products')
        description = data.get('desc_products')
        price = data.get('price_products')
        image = data.get('img_products')  # Este puede ser None
        amount = data.get('cant_products')
        code = data.get('cod_products')
        # Verifica si los parámetros obligatorios están presentes
        if not all([name, description, price]):
            return jsonify({"error": "Faltan parámetros obligatorios"}), 400

        # Si los parámetros opcionales son None, se pueden insertar como NULL en la base de datos
        qagregar = """INSERT INTO products(name_products, desc_products, price_products, img_products,cant_products,cod_products) 
                      VALUES (?, ?, ?, ?, ?,?)"""
        
        # Ejecuta la inserción con los valores, permitiendo que algunos valores sean None (NULL)
        cur.execute(qagregar, (name, description, price, image,amount,code))
        db.commit()
        return jsonify({"message": "Producto creado exitosamente"}), 201

    except mariadb.Error as e:
        return jsonify({"error": "Error en la base de datos", "message": str(e)}), 500
    
    finally:
        if db:
            db.close()