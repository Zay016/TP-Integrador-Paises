"""
Módulo: estadisticas.py
-----------------------
Responsable de calcular indicadores estadísticos a partir de la lista de países:
    - País con mayor y menor población.
    - Promedio de población.
    - Promedio de superficie.
    - Cantidad de países por continente.

Las funciones devuelven datos (no imprimen), así main.py decide cómo mostrarlos.
"""


def pais_mayor_poblacion(paises):
    """
    Devuelve el país con MAYOR población.

    Retorna:
        dict | None: el país, o None si la lista está vacía.
    """
    if not paises:
        return None
    mayor = paises[0]
    for pais in paises:
        if pais["poblacion"] > mayor["poblacion"]:
            mayor = pais
    return mayor


def pais_menor_poblacion(paises):
    """
    Devuelve el país con MENOR población.

    Retorna:
        dict | None: el país, o None si la lista está vacía.
    """
    if not paises:
        return None
    menor = paises[0]
    for pais in paises:
        if pais["poblacion"] < menor["poblacion"]:
            menor = pais
    return menor


def promedio_poblacion(paises):
    """
    Calcula el promedio de población de todos los países.

    Retorna:
        float: promedio (0 si la lista está vacía).
    """
    if not paises:
        return 0
    total = 0
    for pais in paises:
        total += pais["poblacion"]
    return total / len(paises)


def promedio_superficie(paises):
    """
    Calcula el promedio de superficie de todos los países.

    Retorna:
        float: promedio (0 si la lista está vacía).
    """
    if not paises:
        return 0
    total = 0
    for pais in paises:
        total += pais["superficie"]
    return total / len(paises)


def cantidad_por_continente(paises):
    """
    Cuenta cuántos países hay por cada continente.

    Retorna:
        dict: {continente: cantidad}. Ej: {"América": 6, "Asia": 5, ...}
    """
    conteo = {}
    for pais in paises:
        continente = pais["continente"]
        # Si el continente ya está en el diccionario sumamos 1;
        # si no, lo agregamos empezando en 1.
        if continente in conteo:
            conteo[continente] += 1
        else:
            conteo[continente] = 1
    return conteo
