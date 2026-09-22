import os
from typing import Iterable, List, Optional


class GestorCSV:
    def __init__(self, archivo="clientes.csv"):
        self.archivo = archivo

    def escribir(self, tupla):
        with open(self.archivo, "a", encoding="utf-8") as f:
            cadena = ",".join(tupla) + "\n"
            f.write(cadena)

    def leer_primera_fila(self):
        with open(self.archivo, "r", encoding="utf-8") as f:
            linea = f.readline().strip()
            if linea:
                campos = linea.split(",")
                return tuple(campos)
            return ()

    def leer_todas_las_filas(self):
        filas = []
        with open(self.archivo, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea:
                    filas.append(tuple(linea.split(",")))
        return filas


def listar_entradas(ruta: str, mostrar_ocultos: bool = False) -> Iterable[os.DirEntry]:
    with os.scandir(ruta) as it:
        entradas = [e for e in it if mostrar_ocultos or not e.name.startswith(".")]
    entradas.sort(key=lambda e: (e.is_file(), e.name.casefold()))
    return entradas


def dibujar_arbol(
    ruta: str,
    prefijo: str = "",
    mostrar_ocultos: bool = False,
    profundidad_maxima: Optional[int] = None,
    es_ultimo: bool = True,
    es_raiz: bool = True,
) -> List[str]:
    lineas = []

    nombre = os.path.basename(os.path.normpath(ruta)) or ruta
    esquina = "└──" if es_ultimo else "├──"

    if es_raiz:
        lineas.append(nombre)
    else:
        lineas.append(f"{prefijo}{esquina} {nombre}")

    if profundidad_maxima is not None and profundidad_maxima <= 0:
        return lineas

    prefijo_hijos = prefijo + ("    " if es_ultimo else "│   ")

    try:
        entradas = listar_entradas(ruta, mostrar_ocultos=mostrar_ocultos)
    except PermissionError:
        lineas.append(f"{prefijo_hijos}└── (permiso denegado)")
        return lineas
    except FileNotFoundError:
        lineas.append(f"{prefijo_hijos}└── (no encontrado)")
        return lineas

    carpetas = [e for e in entradas if e.is_dir(follow_symlinks=False)]
    archivos = [e for e in entradas if e.is_file(follow_symlinks=False)]
    otros = [
        e
        for e in entradas
        if not e.is_dir(follow_symlinks=False) and not e.is_file(follow_symlinks=False)
    ]

    for i, carpeta in enumerate(carpetas):
        ultimo = (i == len(carpetas) - 1) and not archivos and not otros
        lineas.extend(
            dibujar_arbol(
                carpeta.path,
                prefijo=prefijo_hijos,
                mostrar_ocultos=mostrar_ocultos,
                profundidad_maxima=None if profundidad_maxima is None else profundidad_maxima - 1,
                es_ultimo=ultimo,
                es_raiz=False,
            )
        )

    hojas = archivos + otros
    for i, hoja in enumerate(hojas):
        ultimo = i == len(hojas) - 1
        esquina_hoja = "└──" if ultimo else "├──"
        lineas.append(f"{prefijo_hijos}{esquina_hoja} {hoja.name}")

    return lineas


def guardar_arbol(ruta: str, archivo_salida: str = "tree.txt", mostrar_ocultos: bool = False) -> List[str]:
    lineas = dibujar_arbol(ruta, mostrar_ocultos=mostrar_ocultos)
    with open(archivo_salida, "w", encoding="utf-8") as f:
        f.write("\n".join(lineas))
    return lineas


if __name__ == "__main__":
    print("=" * 60)
    print("DEMOSTRACION DEL BLOQUE A: GestorCSV")
    print("=" * 60)

    gestor = GestorCSV("demo_clientes.csv")
    gestor.escribir(("Jose Vicente", "Carratala", "info@jocarsa.com"))
    gestor.escribir(("Ana", "Garcia", "ana@example.com"))

    print("Primera fila leida:", gestor.leer_primera_fila())
    print("Todas las filas leidas:", gestor.leer_todas_las_filas())

    print()
    print("=" * 60)
    print("DEMOSTRACION DEL BLOQUE B: dibujar_arbol")
    print("=" * 60)

    carpeta_demo = "demo_arbol"
    os.makedirs(os.path.join(carpeta_demo, "primero", "programacion"), exist_ok=True)
    os.makedirs(os.path.join(carpeta_demo, "segundo"), exist_ok=True)
    with open(os.path.join(carpeta_demo, "primero", "notas.txt"), "w") as f:
        f.write("apuntes")
    with open(os.path.join(carpeta_demo, "primero", "programacion", "main.py"), "w") as f:
        f.write("print('hola')")
    with open(os.path.join(carpeta_demo, "segundo", "datos.csv"), "w") as f:
        f.write("a,b,c")

    lineas_arbol = guardar_arbol(carpeta_demo, archivo_salida="demo_tree.txt")
    print("\n".join(lineas_arbol))
    print()
    print("El árbol también se ha guardado en el archivo 'demo_tree.txt'.")
