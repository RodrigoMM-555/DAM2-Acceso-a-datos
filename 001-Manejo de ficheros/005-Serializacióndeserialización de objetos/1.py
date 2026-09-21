import json

NOMBRE_FICHERO = "biblioteca.dat"

def crear_lista_libros():
    libros = [
       {"titulo": "100 papas", "autor": "el", "año": "1999"}, 
       {"titulo": "hola mundo", "autor": "ella", "año": "2010"},
       {"titulo": "paraclama", "autor": "yo", "año": "2002"} 
    ]
    return libros

def serializar_libros(libros):
    cadena = json.dumps(libros)
    print(cadena)
    print(type(cadena))
    return cadena

def guardar_en_fichero(cadena):
    archivo = open(NOMBRE_FICHERO, "w")
    archivo.write(cadena)
    archivo.close

def main():
    libros = crear_lista_libros()
    cadena = serializar_libros(libros)
    guardar_en_fichero(cadena)



if __name__ == "__main__":
    main()
