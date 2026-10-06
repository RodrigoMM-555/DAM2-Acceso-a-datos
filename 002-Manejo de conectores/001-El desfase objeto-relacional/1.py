
import mysql.connector


libros = [
    {"titulo": "Don Quijote", "paginas": 863,
     "generos": ["novela", "aventuras", "humor"]},
    {"titulo": "Platero y yo", "paginas": 144,
     "generos": ["poesía", "infantil"]},
    {"titulo": "Marianela", "paginas": 256,
     "generos": ["novela"]}
]

muestra = libros[0]
for clave in muestra.keys():
    print(clave, type(muestra[clave]))


conn = mysql.connector.connect(
    host="localhost",
    user="desfase",
    password="desfase",
    database="desfase"
)
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS mascotas_vacunas")
cursor.execute("DROP TABLE IF EXISTS mascotas")

'''
cursor.execute("""
CREATE TABLE mascotas (
    Identificador INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    edad INT
)""")


cursor.execute("""
CREATE TABLE mascotas_vacunas (
    Identificador INT AUTO_INCREMENT PRIMARY KEY,
    mascotas_id INT,
    valor VARCHAR(255),
    FOREIGN KEY (mascotas_id) REFERENCES mascotas(Identificador)
)""")


cursor.execute("""
CREATE TABLE mascotas_vacunas (
    Identificador INT AUTO_INCREMENT PRIMARY KEY,
    mascotas_id INT,
    valor VARCHAR(255),
    FOREIGN KEY (mascotas_id) REFERENCES mascotas(Identificador)
)""")



cursor.execute("SELECT Identificador, nombre, edad FROM mascotas")
filas = cursor.fetchall()
 
recuperadas = []
for (id_mascota, nombre, edad) in filas:
    cursor.execute(
        "SELECT valor FROM mascotas_vacunas WHERE mascotas_id = %s",
        (id_mascota,))
    vacunas = [fila[0] for fila in cursor.fetchall()]
    recuperadas.append({"nombre": nombre, "edad": edad, "vacunas": vacunas})
 
print(recuperadas)
conn.close()

'''