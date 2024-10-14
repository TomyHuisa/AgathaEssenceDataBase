from flask import Flask, jsonify, request
import mariadb


app = Flask(__name__)

@app.route('/profiles')
def profiles():
    db = mariadb.connect(
        user="agathaessence",
        password="agathaessence111",
        host="10.9.120.5",
        database="agathaessence"
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM Proffiles")

    profiles = [column[0] for column in cur.description]
    tabla = []
    for row in cur:
        tabla.append(dict(zip(profiles, row)))
    
    return jsonify(tabla)

@app.route("/profiles/<int:id>")
def detalle_profiles(id):
    db = mariadb.connect(
        user="agathaessence",
        password="agathaessence111",
        host="10.9.120.5",
        database="agathaessence"
    )
    cur = db.cursor()
    cur.execute("SELECT first_name, last_name FROM Proffiles WHERE id_profile = ?", (id,))
    profiles = [column[0] for column in cur.description]
    tabla = [dict(zip(profiles, row))for row in cur.fetchall()]
    return jsonify(tabla)