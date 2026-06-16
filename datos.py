"""
Módulo: datos.py
----------------
Responsable de TODO lo relacionado con los datos en sí:
    - Leer el dataset desde el archivo CSV.
    - Guardar los cambios en el CSV (persistencia).
    - Agregar un país nuevo a la lista.
    - Actualizar la población y la superficie de un país existente.

Cada país se representa como un DICCIONARIO con las claves:
    {"nombre": str, "poblacion": int, "superficie": int, "continente": str}

Todos los países juntos forman una LISTA de diccionarios.
"""

import csv

# Encabezados (columnas) que debe tener el archivo CSV.
CAMPOS = ["nombre", "poblacion", "superficie", "continente"]


def cargar_paises(ruta):
    """
    Lee el archivo CSV y devuelve una lista de diccionarios.
    Controla errores de formato (filas incompletas o con números inválidos)
    y avisa por pantalla cuáles filas se ignoraron, sin frenar el programa.

    Parámetros:
        ruta (str): ruta del archivo CSV.

    Retorna:
        list: lista de países (diccionarios). Puede estar vacía si falla todo.
    """
    paises = []
    try:
        with open(ruta, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            numero_fila = 1  # la fila 1 es el encabezado
            for fila in lector:
                numero_fila += 1
                try:
                    pais = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"].strip(),
                    }
                    # No se permiten campos de texto vacíos.
                    if pais["nombre"] == "" or pais["continente"] == "":
                        print(f"⚠️  Fila {numero_fila} ignorada: hay campos vacíos.")
                        continue
                    paises.append(pais)
                except (ValueError, KeyError, TypeError):
                    # ValueError: población/superficie no son números.
                    # KeyError: falta una columna.
                    print(f"⚠️  Fila {numero_fila} ignorada: formato incorrecto.")
    except FileNotFoundError:
        print(f"❌ No se encontró el archivo '{ruta}'. Se inicia con la lista vacía.")
    except OSError:
        print(f"❌ No se pudo abrir el archivo '{ruta}'. Se inicia con la lista vacía.")

    return paises


def guardar_paises(ruta, paises):
    """
    Guarda la lista de países en el archivo CSV (sobrescribe el contenido).
    Se usa después de agregar o actualizar para que los cambios queden guardados.

    Parámetros:
        ruta (str): ruta del archivo CSV.
        paises (list): lista de diccionarios de países.

    Retorna:
        bool: True si se guardó bien, False si hubo un error.
    """
    try:
        with open(ruta, mode="w", encoding="utf-8", newline="") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
            escritor.writeheader()
            escritor.writerows(paises)
        return True
    except OSError:
        print(f"❌ No se pudo guardar el archivo '{ruta}'.")
        return False


def agregar_pais(paises, nombre, poblacion, superficie, continente):
    """
    Crea el diccionario del país nuevo y lo agrega a la lista.
    (La validación de los datos ya se hizo antes, en el módulo de validaciones).

    Retorna:
        dict: el país que se agregó.
    """
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente,
    }
    paises.append(nuevo_pais)
    return nuevo_pais


def actualizar_pais(paises, nombre, nueva_poblacion, nueva_superficie):
    """
    Busca un país por nombre (exacto, sin distinguir mayúsculas) y actualiza
    su población y su superficie.

    Retorna:
        dict | None: el país actualizado, o None si no se encontró.
    """
    nombre = nombre.strip().lower()
    for pais in paises:
        if pais["nombre"].lower() == nombre:
            pais["poblacion"] = nueva_poblacion
            pais["superficie"] = nueva_superficie
            return pais
    return None
