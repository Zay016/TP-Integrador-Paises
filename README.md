# 🌍 Gestión de Datos de Países en Python

Sistema de gestión de países en Python con búsquedas, filtros, ordenamientos y estadísticas.

Aplicación de consola en Python para **gestionar información de países**: permite
cargar datos desde un archivo CSV, agregar y actualizar países, buscar, filtrar,
ordenar y calcular estadísticas, aplicando listas, diccionarios, funciones,
condicionales, ordenamientos y estadísticas básicas.

---

## 📑 Índice
- [Datos del proyecto](#-datos-del-proyecto)
- [Integrantes](#-integrantes)
- [Descripción](#-descripción)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Requisitos](#-requisitos)
- [Instrucciones de ejecución](#-instrucciones-de-ejecución)
- [Funcionalidades](#-funcionalidades)
- [Ejemplos de entrada y salida](#-ejemplos-de-entrada-y-salida)
- [Enlaces](#-enlaces)

---

## 🎓 Datos del proyecto
- **Universidad:** Universidad Tecnológica Nacional (UTN)
- **Carrera:** Tecnicatura Universitaria en Programación a Distancia (TUPAD)
- **Materia:** Programación 1 — 2.º Cuatrimestre 2025
- **Proyecto:** Gestión de Datos de Países en Python: filtros, ordenamientos y estadísticas
- **Profesores:** *[Completar con el/los nombre/s del equipo docente]*

## 👥 Integrantes
| Nombre y Apellido | Tareas principales |
|---|---|
| *[Integrante 1]* | *[Ej.: módulos de datos, validaciones y main]* |
| *[Integrante 2]* | *[Ej.: módulos de filtros, ordenamiento y estadísticas]* |

---

## 📝 Descripción
El sistema gestiona un conjunto de países. Cada país se representa con un
**diccionario** y el conjunto completo se almacena en una **lista**. Los datos de
cada país son:

- **nombre** (texto)
- **poblacion** (entero)
- **superficie** en km² (entero)
- **continente** (texto)

Al iniciar, el programa lee el dataset desde `paises.csv`. Todas las operaciones
se realizan desde un **menú interactivo en consola**.

## 📂 Estructura del proyecto
```
tpi_paises/
├── main.py            # Menú principal (Bloque Main): integra todos los módulos
├── datos.py           # Lectura/escritura del CSV, alta y actualización de países
├── validaciones.py    # Validación y lectura segura de las entradas del usuario
├── busquedas.py       # Búsqueda de países por nombre (parcial o exacta)
├── filtros.py         # Filtros por continente y por rangos de población/superficie
├── ordenamiento.py    # Ordenamiento por nombre, población o superficie (bubble sort)
├── estadisticas.py    # País mayor/menor población, promedios y conteo por continente
├── paises.csv         # Dataset base de países
└── README.md          # Este archivo
```

## ⚙️ Requisitos
- **Python 3.x** (probado en Python 3.12)
- No requiere instalar librerías externas: usa solo la librería estándar (`csv`).

## ▶️ Instrucciones de ejecución
1. Cloná o descargá el repositorio.
2. Abrí una terminal en la carpeta del proyecto (donde está `main.py`).
3. Ejecutá:

```bash
python main.py
```
> En algunos sistemas el comando es `python3 main.py`.

4. Usá el menú escribiendo el número de la opción y presionando Enter.

> ℹ️ **Importante:** ejecutá el programa desde la misma carpeta donde está
> `paises.csv`, para que pueda encontrar el dataset.

## 🧩 Funcionalidades
El menú permite:

1. **Mostrar** todos los países.
2. **Agregar** un país (no se permiten campos vacíos ni países repetidos).
3. **Actualizar** la población y la superficie de un país existente.
4. **Buscar** un país por nombre (coincidencia parcial o exacta).
5. **Filtrar** países por:
   - Continente
   - Rango de población
   - Rango de superficie
6. **Ordenar** países por nombre, población o superficie (ascendente o descendente).
7. **Estadísticas:**
   - País con mayor y menor población
   - Promedio de población
   - Promedio de superficie
   - Cantidad de países por continente

Incluye **validaciones** y **manejo de errores**: filas mal formateadas en el CSV
se ignoran sin frenar el programa, las entradas no numéricas se rechazan y las
búsquedas/filtros sin resultados muestran un mensaje claro.

## 💻 Ejemplos de entrada y salida

**Estadísticas (opción 7):**
```
=== ESTADÍSTICAS ===

  🌍 País con MAYOR población:
  China                | Pob: 1,402,112,000 | Sup:    9,596,961 km² | Asia

  🏝️  País con MENOR población:
  Nueva Zelanda        | Pob:     4,822,233 | Sup:      270,467 km² | Oceanía

  📊 Promedio de población : 223,222,588 habitantes
  📐 Promedio de superficie: 3,621,048 km²

  🗺️  Cantidad de países por continente:
     - América     : 6
     - Asia        : 5
     - Europa      : 6
     - África      : 3
     - Oceanía     : 2
```

**Filtrar por continente (opción 5 → 1 → "Europa"):**
```
--- Países de Europa (6 país/es) ---
  Alemania             | Pob:    83,149,300 | Sup:      357,022 km² | Europa
  Francia              | Pob:    67,391,582 | Sup:      551,695 km² | Europa
  España               | Pob:    47,351,567 | Sup:      505,990 km² | Europa
  ...
```

**Buscar (opción 4 → "arg", parcial):**
```
--- Resultados de la búsqueda 'arg' (1 país/es) ---
  Argentina            | Pob:    45,376,763 | Sup:    2,780,400 km² | América
```

## 🔗 Enlaces
- **Repositorio GitHub:** *[Pegar el link del repositorio]*
- **Video explicativo (10-15 min):** *[Pegar el link público del video — YouTube/Drive]*
- **Documentación (PDF):** disponible en la raíz del repositorio.
