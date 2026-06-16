"""
Módulo: ordenamiento.py
-----------------------
Responsable de ordenar la lista de países según distintos criterios:
    - Por nombre (alfabético).
    - Por población.
    - Por superficie.
En todos los casos se puede elegir orden ascendente o descendente.

Se implementa el algoritmo de ordenamiento "burbuja" (bubble sort) de forma
manual para mostrar cómo funciona un ordenamiento por dentro. La versión
"pythónica" equivalente sería usar sorted(paises, key=..., reverse=...).
"""


def ordenar_paises(paises, clave, descendente=False):
    """
    Ordena una lista de países usando el algoritmo burbuja.

    Parámetros:
        paises (list): lista de diccionarios de países.
        clave (str): por qué campo ordenar -> "nombre", "poblacion" o "superficie".
        descendente (bool): True para mayor a menor; False (por defecto) para menor a mayor.

    Retorna:
        list: una lista NUEVA ordenada (no modifica la original).
    """
    # Trabajamos sobre una copia para no alterar la lista original.
    lista = paises.copy()
    cantidad = len(lista)

    # Algoritmo burbuja: recorre la lista comparando elementos contiguos
    # y los intercambia si están en el orden equivocado.
    for i in range(cantidad - 1):
        for j in range(cantidad - 1 - i):
            valor_actual = lista[j][clave]
            valor_siguiente = lista[j + 1][clave]

            # Si la clave es texto (nombre), comparamos en minúsculas
            # para que el orden alfabético no se vea afectado por mayúsculas.
            if isinstance(valor_actual, str):
                valor_actual = valor_actual.lower()
                valor_siguiente = valor_siguiente.lower()

            if descendente:
                hay_que_intercambiar = valor_actual < valor_siguiente
            else:
                hay_que_intercambiar = valor_actual > valor_siguiente

            if hay_que_intercambiar:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista
