"""
Módulo: filtros.py
------------------
Responsable de filtrar la lista de países según distintos criterios:
    - Por continente.
    - Por rango de población.
    - Por rango de superficie.

Cada función devuelve una lista NUEVA con los países que cumplen la condición,
sin modificar la lista original.
"""


def filtrar_por_continente(paises, continente):
    """
    Devuelve los países que pertenecen al continente indicado
    (sin distinguir mayúsculas/minúsculas).

    Retorna:
        list: países del continente buscado.
    """
    continente = continente.strip().lower()
    resultados = []
    for pais in paises:
        if pais["continente"].lower() == continente:
            resultados.append(pais)
    return resultados


def filtrar_por_rango_poblacion(paises, minimo, maximo):
    """
    Devuelve los países cuya población está entre 'minimo' y 'maximo'
    (ambos incluidos).

    Retorna:
        list: países dentro del rango de población.
    """
    resultados = []
    for pais in paises:
        if minimo <= pais["poblacion"] <= maximo:
            resultados.append(pais)
    return resultados


def filtrar_por_rango_superficie(paises, minimo, maximo):
    """
    Devuelve los países cuya superficie está entre 'minimo' y 'maximo'
    (ambos incluidos).

    Retorna:
        list: países dentro del rango de superficie.
    """
    resultados = []
    for pais in paises:
        if minimo <= pais["superficie"] <= maximo:
            resultados.append(pais)
    return resultados
