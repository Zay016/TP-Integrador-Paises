"""
Módulo: busquedas.py
--------------------
Responsable de buscar países dentro de la lista.
Permite buscar por nombre con coincidencia parcial o exacta.
"""


def buscar_por_nombre(paises, termino, exacta=False):
    """
    Busca países cuyo nombre coincida con el término ingresado.

    Parámetros:
        paises (list): lista de diccionarios de países.
        termino (str): texto a buscar.
        exacta (bool): si es True busca coincidencia exacta;
                       si es False (por defecto) busca coincidencia parcial.

    Retorna:
        list: lista de países que coinciden (puede estar vacía).
    """
    termino = termino.strip().lower()
    resultados = []

    for pais in paises:
        nombre = pais["nombre"].lower()
        if exacta:
            if nombre == termino:
                resultados.append(pais)
        else:
            # Coincidencia parcial: el término está contenido en el nombre.
            if termino in nombre:
                resultados.append(pais)

    return resultados
