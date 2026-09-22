NOMBRE_FICHERO_TEMPERATURAS = "temperaturas.txt"
NOMBRE_FICHERO_CONTADOR = "contador.bin"

def escribir_temperaturas():
    print("-------------------")
    fichero = open(NOMBRE_FICHERO_TEMPERATURAS, "w")
    fichero.write("18.5\n21.0\n19.2")
    fichero.close()
    pass

def leer_temperaturas():
    print("-------------------")

    fichero = open(NOMBRE_FICHERO_TEMPERATURAS, "r")
    datos = fichero.read()
    fichero.close()
    print(datos)
    pass

def saltar_primera_temperatura():
    print("-------------------")

    fichero = open(NOMBRE_FICHERO_TEMPERATURAS, "r")
    fichero.readline()
    posicion = fichero.tell()
    print(posicion)
    fichero.seek(0)
    posicionOriginal = fichero.tell()
    print(posicionOriginal)
    fichero.seek(posicion)
    posicion = fichero.tell()
    print(posicion)
    resto = fichero.read()
    fichero.close()
    print(resto)
    pass

def comprobar_fichero_configuracion():
    print("-------------------")
    try:
        flujo = open("configuracion.txt", "r")
        flujo.close()
    except FileNotFoundError:
        print("Error controlado: el fichero no existe, pero el programa no se cae.")
    pass

def guardar_numero_registros():
    print("-------------------")
    binario = bytes([3])
    fichero_binario = open(NOMBRE_FICHERO_CONTADOR, "wb")
    fichero_binario.write(binario)
    fichero_binario.close()
    fichero_binario = open(NOMBRE_FICHERO_CONTADOR, "rb")
    datosb = fichero_binario.read()
    fichero_binario.close
    print(list(datosb))
    pass

def main():
    escribir_temperaturas()
    leer_temperaturas()
    leer_temperaturas()
    saltar_primera_temperatura()
    comprobar_fichero_configuracion()
    guardar_numero_registros()
    pass

if __name__ == "__main__":
    main()