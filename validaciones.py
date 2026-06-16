"""
Módulo: validaciones.py
-----------------------
Contiene funciones encargadas de validar y leer de forma segura los datos
que ingresa el usuario por consola. Su responsabilidad es garantizar que el
resto del programa siempre reciba datos correctos (sin campos vacíos, números
válidos, rangos coherentes), mostrando mensajes claros de error.

Una función = una responsabilidad.
"""


def leer_texto(mensaje):
    """
    Pide un texto por teclado y no lo acepta hasta que el usuario escriba
    algo que no esté vacío (no se permiten campos vacíos).

    Parámetros:
        mensaje (str): texto que se muestra al usuario.

    Retorna:
        str: el texto ingresado, sin espacios sobrantes al inicio/final.
    """
    while True:
        valor = input(mensaje).strip()
        if valor != "":
            return valor
        print("⚠️  El campo no puede estar vacío. Intentá de nuevo.")


def leer_entero_positivo(mensaje):
    """
    Pide un número entero mayor o igual a 0. Si el usuario escribe algo que
    no es un número, vuelve a pedirlo (manejo de errores con try/except).

    Parámetros:
        mensaje (str): texto que se muestra al usuario.

    Retorna:
        int: el número entero válido ingresado.
    """
    while True:
        entrada = input(mensaje).strip()
        try:
            numero = int(entrada)
            if numero < 0:
                print("⚠️  El número no puede ser negativo. Intentá de nuevo.")
                continue
            return numero
        except ValueError:
            print("⚠️  Eso no es un número entero válido. Intentá de nuevo.")


def leer_rango(mensaje_min, mensaje_max):
    """
    Pide un valor mínimo y uno máximo y se asegura de que el mínimo no sea
    mayor que el máximo. Si lo es, se intercambian automáticamente para que
    el rango siempre sea coherente.

    Retorna:
        tuple: (minimo, maximo) ya ordenados.
    """
    minimo = leer_entero_positivo(mensaje_min)
    maximo = leer_entero_positivo(mensaje_max)
    if minimo > maximo:
        # Si el usuario los ingresó al revés, los acomodamos.
        minimo, maximo = maximo, minimo
    return minimo, maximo


def existe_pais(paises, nombre):
    """
    Indica si ya existe un país con ese nombre en la lista (sin distinguir
    mayúsculas/minúsculas). Sirve para no cargar países repetidos.

    Parámetros:
        paises (list): lista de diccionarios de países.
        nombre (str): nombre a buscar.

    Retorna:
        bool: True si existe, False si no.
    """
    nombre = nombre.strip().lower()
    for pais in paises:
        if pais["nombre"].lower() == nombre:
            return True
    return False
