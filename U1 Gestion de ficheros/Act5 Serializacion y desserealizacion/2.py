import json
 
NOMBRE_FICHERO = "biblioteca.dat"
 
def leer_fichero():
    fichero = open(NOMBRE_FICHERO, "r")
    linea = fichero.readlines()[0]
    print(linea)
    print(type(linea))
    fichero.close
    return linea
 
def deserializar_libros(linea):
    deserealizada = json.loads(linea)
    print(deserealizada)
    print(type(deserealizada))


def main():
    linea = leer_fichero()
    deserializar_libros(linea)

if __name__ == "__main__":
    main()