"""
Módulo: main.py  (Bloque Main)
------------------------------
Punto de entrada del programa. Muestra el menú principal en consola y
coordina los demás módulos:
    - datos        -> cargar/guardar CSV, agregar y actualizar países.
    - validaciones -> leer entradas seguras.
    - busquedas    -> buscar por nombre.
    - filtros      -> filtrar por continente / población / superficie.
    - ordenamiento -> ordenar por nombre / población / superficie.
    - estadisticas -> indicadores del dataset.

Para ejecutar:  python main.py
"""

import datos
import validaciones
import busquedas
import filtros
import ordenamiento
import estadisticas

# Nombre del archivo donde está (y se guarda) el dataset.
ARCHIVO_CSV = "paises.csv"


# ----------------------------------------------------------------------
# Funciones de presentación (mostrar datos por pantalla)
# ----------------------------------------------------------------------

def mostrar_pais(pais):
    """Muestra los datos de un país con formato de tabla y números legibles."""
    print(
        f"  {pais['nombre']:<20} | "
        f"Pob: {pais['poblacion']:>13,} | "
        f"Sup: {pais['superficie']:>12,} km² | "
        f"{pais['continente']}"
    )


def mostrar_lista(paises, titulo="Resultado"):
    """
    Muestra una lista de países. Si la lista está vacía, avisa con un mensaje
    claro en lugar de mostrar una tabla vacía.
    """
    print(f"\n--- {titulo} ({len(paises)} país/es) ---")
    if not paises:
        print("  (No hay países para mostrar.)")
        return
    for pais in paises:
        mostrar_pais(pais)


def pausar():
    """Pausa la ejecución hasta que el usuario presione Enter."""
    input("\nPresioná Enter para continuar...")


# ----------------------------------------------------------------------
# Opciones del menú (cada una es una responsabilidad)
# ----------------------------------------------------------------------

def opcion_agregar(paises):
    """Agrega un país nuevo, validando que no haya campos vacíos ni repetidos."""
    print("\n=== AGREGAR PAÍS ===")
    nombre = validaciones.leer_texto("Nombre del país: ")

    # Evitamos cargar un país que ya existe.
    if validaciones.existe_pais(paises, nombre):
        print(f"⚠️  El país '{nombre}' ya existe. No se agregó.")
        return

    poblacion = validaciones.leer_entero_positivo("Población: ")
    superficie = validaciones.leer_entero_positivo("Superficie (km²): ")
    continente = validaciones.leer_texto("Continente: ")

    datos.agregar_pais(paises, nombre, poblacion, superficie, continente)
    datos.guardar_paises(ARCHIVO_CSV, paises)
    print(f"✅ País '{nombre}' agregado y guardado correctamente.")


def opcion_actualizar(paises):
    """Actualiza la población y la superficie de un país existente."""
    print("\n=== ACTUALIZAR PAÍS ===")
    nombre = validaciones.leer_texto("Nombre del país a actualizar: ")

    if not validaciones.existe_pais(paises, nombre):
        print(f"⚠️  No existe ningún país llamado '{nombre}'.")
        return

    nueva_poblacion = validaciones.leer_entero_positivo("Nueva población: ")
    nueva_superficie = validaciones.leer_entero_positivo("Nueva superficie (km²): ")

    actualizado = datos.actualizar_pais(
        paises, nombre, nueva_poblacion, nueva_superficie
    )
    if actualizado:
        datos.guardar_paises(ARCHIVO_CSV, paises)
        print(f"✅ País '{actualizado['nombre']}' actualizado correctamente.")
    else:
        print("⚠️  No se pudo actualizar el país.")


def opcion_buscar(paises):
    """Busca un país por nombre (parcial o exacto)."""
    print("\n=== BUSCAR PAÍS ===")
    termino = validaciones.leer_texto("Nombre (o parte del nombre) a buscar: ")
    print("¿Coincidencia exacta? (s/n): ", end="")
    exacta = input().strip().lower() == "s"

    resultados = busquedas.buscar_por_nombre(paises, termino, exacta)
    mostrar_lista(resultados, f"Resultados de la búsqueda '{termino}'")


def opcion_filtrar(paises):
    """Submenú de filtros: continente, rango de población o rango de superficie."""
    print("\n=== FILTRAR PAÍSES ===")
    print("  1. Por continente")
    print("  2. Por rango de población")
    print("  3. Por rango de superficie")
    opcion = validaciones.leer_texto("Elegí una opción: ")

    if opcion == "1":
        continente = validaciones.leer_texto("Continente: ")
        resultados = filtros.filtrar_por_continente(paises, continente)
        mostrar_lista(resultados, f"Países de {continente}")
    elif opcion == "2":
        minimo, maximo = validaciones.leer_rango(
            "Población mínima: ", "Población máxima: "
        )
        resultados = filtros.filtrar_por_rango_poblacion(paises, minimo, maximo)
        mostrar_lista(resultados, f"Población entre {minimo:,} y {maximo:,}")
    elif opcion == "3":
        minimo, maximo = validaciones.leer_rango(
            "Superficie mínima (km²): ", "Superficie máxima (km²): "
        )
        resultados = filtros.filtrar_por_rango_superficie(paises, minimo, maximo)
        mostrar_lista(resultados, f"Superficie entre {minimo:,} y {maximo:,} km²")
    else:
        print("⚠️  Opción de filtro inválida.")


def opcion_ordenar(paises):
    """Submenú de ordenamiento: por nombre, población o superficie, asc/desc."""
    print("\n=== ORDENAR PAÍSES ===")
    print("  1. Por nombre")
    print("  2. Por población")
    print("  3. Por superficie")
    opcion = validaciones.leer_texto("Elegí una opción: ")

    claves = {"1": "nombre", "2": "poblacion", "3": "superficie"}
    if opcion not in claves:
        print("⚠️  Opción de ordenamiento inválida.")
        return

    clave = claves[opcion]
    print("¿Orden descendente (mayor a menor)? (s/n): ", end="")
    descendente = input().strip().lower() == "s"

    ordenados = ordenamiento.ordenar_paises(paises, clave, descendente)
    sentido = "descendente" if descendente else "ascendente"
    mostrar_lista(ordenados, f"Países ordenados por {clave} ({sentido})")


def opcion_estadisticas(paises):
    """Muestra todas las estadísticas del dataset."""
    print("\n=== ESTADÍSTICAS ===")
    if not paises:
        print("  (No hay países cargados para calcular estadísticas.)")
        return

    mayor = estadisticas.pais_mayor_poblacion(paises)
    menor = estadisticas.pais_menor_poblacion(paises)
    prom_pob = estadisticas.promedio_poblacion(paises)
    prom_sup = estadisticas.promedio_superficie(paises)
    por_continente = estadisticas.cantidad_por_continente(paises)

    print(f"\n  🌍 País con MAYOR población:")
    mostrar_pais(mayor)
    print(f"\n  🏝️  País con MENOR población:")
    mostrar_pais(menor)
    print(f"\n  📊 Promedio de población : {prom_pob:,.0f} habitantes")
    print(f"  📐 Promedio de superficie: {prom_sup:,.0f} km²")
    print(f"\n  🗺️  Cantidad de países por continente:")
    for continente, cantidad in por_continente.items():
        print(f"     - {continente:<12}: {cantidad}")


def mostrar_menu():
    """Imprime el menú principal de opciones."""
    print("\n" + "=" * 50)
    print("   GESTIÓN DE DATOS DE PAÍSES - Programación 1")
    print("=" * 50)
    print("  1. Mostrar todos los países")
    print("  2. Agregar un país")
    print("  3. Actualizar un país")
    print("  4. Buscar un país por nombre")
    print("  5. Filtrar países")
    print("  6. Ordenar países")
    print("  7. Mostrar estadísticas")
    print("  0. Salir")
    print("=" * 50)


# ----------------------------------------------------------------------
# Programa principal
# ----------------------------------------------------------------------

def main():
    """Función principal: carga los datos y ejecuta el bucle del menú."""
    print("Cargando dataset de países...")
    paises = datos.cargar_paises(ARCHIVO_CSV)
    print(f"✅ Se cargaron {len(paises)} países.")

    while True:
        mostrar_menu()
        opcion = validaciones.leer_texto("Elegí una opción: ")

        if opcion == "1":
            mostrar_lista(paises, "Todos los países")
        elif opcion == "2":
            opcion_agregar(paises)
        elif opcion == "3":
            opcion_actualizar(paises)
        elif opcion == "4":
            opcion_buscar(paises)
        elif opcion == "5":
            opcion_filtrar(paises)
        elif opcion == "6":
            opcion_ordenar(paises)
        elif opcion == "7":
            opcion_estadisticas(paises)
        elif opcion == "0":
            print("\n¡Gracias por usar el sistema! Hasta luego. 👋")
            break
        else:
            print("⚠️  Opción inválida. Elegí un número del menú.")

        pausar()


# Esto hace que main() se ejecute solo si corremos este archivo directamente.
if __name__ == "__main__":
    main()
