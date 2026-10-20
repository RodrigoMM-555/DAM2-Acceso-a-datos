import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="accesoadatos2526",
    password="Accesoadatos2526$",
    database="accesoadatos2526"
)

cursor = conexion.cursor()

cursor.execute(
    "INSERT INTO clientes (nombre, apellidos, email) VALUES (%s, %s, %s)",
    ("Ana", "Martinez Ruiz", "ana@martinezruiz.com")
)

conexion.commit()

identificador_ana = cursor.lastrowid
print("Clienta insertada correctamente. Identificador:", identificador_ana)

cursor.execute("SELECT * FROM clientes")
for fila in cursor.fetchall():
    print(fila)

cursor.close()
conexion.close()



