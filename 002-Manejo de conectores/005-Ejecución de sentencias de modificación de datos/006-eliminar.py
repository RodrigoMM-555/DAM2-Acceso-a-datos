import mysql.connector

# Según el enunciado, Ana tiene el identificador 4.
# Si recibió otro identificador, cambia el valor de esta variable.
identificador_ana = 4

conexion = mysql.connector.connect(
    host="localhost",
    user="accesoadatos2526",
    password="Accesoadatos2526$",
    database="accesoadatos2526"
)

cursor = conexion.cursor()

cursor.execute(
    "DELETE FROM clientes WHERE Identificador = %s",
    (identificador_ana,)
)

conexion.commit()
print("Registros eliminados:", cursor.rowcount)

cursor.execute("SELECT * FROM clientes")
for fila in cursor.fetchall():
    print(fila)

cursor.close()
conexion.close()
