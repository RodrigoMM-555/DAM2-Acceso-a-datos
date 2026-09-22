

tuplas = [
    ("Rodrigo", 20, "Valencia"),
    ("Ana", 21, "Madrid"),
    ("Carlos", 19, "Barcelona")
]


import os
 
NOMBRE_FICHERO_NOTAS = "notas.csv"
CARPETA_PRACTICAS = "practicas"
NOMBRE_FICHERO_ESTRUCTURA = "estructura_practicas.txt"
 
def guardar_notas():
    with open(NOMBRE_FICHERO_NOTAS, "w", encoding="utf-8") as notas:
        for tupla in tuplas:
            cadena = ",".join(map(str, tupla)) + "\n"
            notas.write(cadena)
    notas.close()
 

def leer_notas():
    with open(NOMBRE_FICHERO_NOTAS, "r", encoding="utf-8") as notas:
        listaTuplas = []

        for linea in notas: #No es necesario el readlines
            linea = linea.strip()
            listaTuplas.append(tuple(linea.split(",")))

    print(listaTuplas)
    notas.close()
    return listaTuplas

 
def crear_carpetas_de_prueba():




def dibujar_estructura_practicas(ruta):
    # tu codigo aqui
    pass
 
def guardar_estructura_practicas(ruta, archivo_salida=NOMBRE_FICHERO_ESTRUCTURA):
    # tu codigo aqui
    pass
 
def main():
    guardar_notas()
    leer_notas()
    crear_carpetas_de_prueba()
    dibujar_estructura_practicas(CARPETA_PRACTICAS)
    guardar_estructura_practicas(CARPETA_PRACTICAS)

 
if __name__ == "__main__":
    main()