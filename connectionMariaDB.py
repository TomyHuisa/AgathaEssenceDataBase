import mariadb


conn = mariadb.connect(
    user="agathaessence",
    password="agathaessence111",
    host="10.9.120.5",
    database="agathaessence"
)

cur = conn.cursor()
cur.execute("SELECT * FROM users")

#Obtener los nombres de las columnas 
users = [column[0] for column in cur.description] 

#Almacenar los resultados en una lista de diccionarios
tabla = []
for row in cur:
    tabla.append(dict(zip(users, row)))

#CERRAR LA CONEXIÒN
mariadb.close()
#imprimir los resultados
print(tabla)