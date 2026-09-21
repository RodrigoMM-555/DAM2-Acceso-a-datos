
import csv
import json


def leer_csv(ruta_csv):
    """Paso 1 y 2: lee el CSV y devuelve una lista de diccionarios."""
    contactos = []

    with open(ruta_csv, mode="r", encoding="utf-8-sig", newline="") as archivo_csv:
        lector = csv.DictReader(archivo_csv, delimiter=";")

        for fila in lector:
            contacto = {
                "planeta": fila["Column1"],
                "masa": fila["Mass (1024kg)"],
                "diametro": fila["Diameter (km)"],
                "densidad": fila["Density (kg/m3)"],
                "gravedad": fila["Gravity (m/s2)"],
                "velocidad_escape": fila["Escape Velocity (km/s)"],
                "periodo_rotacion": fila["Rotation Period (hours)"],
                "duracion_dia": fila["Length of Day (hours)"],
                "distancia_sol": fila["Distance from Sun (106 km)"],
                "perihelio": fila["Perihelion (106 km)"],
                "afelio": fila["Aphelion (106 km)"],
                "periodo_orbital": fila["Orbital Period (days)"],
                "velocidad_orbital": fila["Orbital Velocity (km/s)"],
                "inclinacion_orbital": fila["Orbital Inclination (degrees)"],
                "excentricidad_orbital": fila["Orbital Eccentricity"],
                "oblicuidad_orbita": fila["Obliquity to Orbit (degrees)"],
                "temperatura_media": fila["Mean Temperature (C)"],
                "presion_superficie": fila["Surface Pressure (bars)"],
                "numero_lunas": fila["Number of Moons"],
                "sistema_anillos": fila["Ring System?"],
                "campo_magnetico": fila["Global Magnetic Field?"],
                "planeta_repetido": fila["_1"],
            }
            contactos.append(contacto)

    print (contactos)
    return contactos


def guardar_json(contactos, ruta_json):
    """Paso 3: guarda la lista de diccionarios en un archivo JSON legible."""
    with open(ruta_json, mode="w", encoding="utf-8") as archivo_json:
        json.dump(contactos, archivo_json, indent=4, ensure_ascii=False)    #ascii=false permite que hayan tildes y ñ


def escribir_log(contactos, ruta_log):
    """Paso 4: escribe una línea de log por cada contacto procesado."""
    with open(ruta_log, mode="w", encoding="utf-8") as archivo_log:
        for contacto in contactos:
            linea = f"Planeta añadido: {contacto['planeta']}\n"
            archivo_log.write(linea)


def contar_lineas_log(ruta_log):
    """Paso 5: abre el log.txt y cuenta cuántas líneas (contactos) tiene."""
    with open(ruta_log, mode="r", encoding="utf-8") as archivo_log:
        lineas = archivo_log.readlines()
    return len(lineas)


def main():
    ruta_csv = "NASA.csv"
    ruta_json = "Planetas.json"
    ruta_log = "log.txt"

    # 1 y 2. Leer el CSV y convertir cada fila en un diccionario
    contactos = leer_csv(ruta_csv)
    print(f"Se han leído {len(contactos)} contactos desde '{ruta_csv}'.")

    # 3. Guardar todos los contactos en contactos.json
    guardar_json(contactos, ruta_json)
    print(f"Contactos guardados en '{ruta_json}'.")

    # 4. Escribir log.txt con una línea por contacto
    escribir_log(contactos, ruta_log)
    print(f"Registro de actividad escrito en '{ruta_log}'.")

    # 5. Leer log.txt y mostrar cuántas líneas (contactos) se han procesado
    total = contar_lineas_log(ruta_log)
    print(f"\nTotal de contactos procesados según el log: {total}")


if __name__ == "__main__":
    main()