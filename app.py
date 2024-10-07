from flask import Flask, jsonify, request
import sys
import mariadb

try:
    conn = mariadb.connect(
        user="agathaessence",
        password="agathaessence111",
        host="10.9.120.5",
        port=8080,
        database="agathaessence"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)


app = Flask(__name__)


@app.route('/profiles')
def profiles():
    db = mariadb.connect(db_file, detect_types=mariadb.PARSE_DECLTYPES)
    db.row_factory =dict_factory
    #CONSULTA
    query= "SELECT * FROM proffiles"
    result= db.execute(query)
    #CONVERTIR OBJETO CURSOR A LISTA
    result= list(result)
    #CERRAR LA CONEXIÓN
    db.close()

    return jsonify(result)

@app.route("/profiles/<int:id>")
def detalle_profiles(id):
    db = profiles.connect(db_file,detect_types=profiles.PARSE_DECLTYPES)
    db.row_factory = dict_factory
    #CONSULTA 1
    qnombre= "SELECT first_name, last_name FROM proffiles WHERE id_profile = ?"