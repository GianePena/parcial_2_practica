# 📚 Sistema de Gestión de Alumnos

> Sistema CRUD completo para la administración de estudiantes organizado por años académicos y turnos, con almacenamiento en archivos CSV.

## 📋 Tabla de Contenidos

- [Descripción](#-descripción)
- [Características](#-características)
- [Requisitos](#-requisitos)
- [Instalación](#-instalación)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Uso](#-uso)
- [Funcionalidades Detalladas](#-funcionalidades-detalladas)
- [Arquitectura del Código](#-arquitectura-del-código)
- [Validaciones y Seguridad](#-validaciones-y-seguridad)
- [Manejo de Errores](#-manejo-de-errores)
- [Ejemplos](#-ejemplos)
- [Autores](#-autores)

## 🎯 Descripción

Sistema de gestión estudiantil desarrollado en Python para administrar información de alumnos de manera organizada y eficiente. La aplicación permite realizar operaciones CRUD (Create, Read, Update, Delete) sobre registros de estudiantes distribuidos en tres años académicos, cada uno con turnos de mañana y tarde.

### ¿Por qué este proyecto?

- **Organización jerárquica**: Datos estructurados por año y turno
- **Persistencia de datos**: Almacenamiento en archivos CSV
- **Interfaz simple**: Menú de consola intuitivo
- **Validaciones robustas**: Control de integridad de datos
- **Modular y mantenible**: Código organizado en módulos separados

## ✨ Características

- ✅ Listado completo de estudiantes
- ✅ Filtrado por año académico
- ✅ Alta de nuevos alumnos
- ✅ Modificación de datos existentes
- ✅ Eliminación de registros
- ✅ Validación de IDs únicos
- ✅ Manejo automático de archivos CSV
- ✅ Normalización de datos
- ✅ Búsqueda eficiente por identificador

## 💻 Requisitos

```
Python >= 3.10
```

### Librerías estándar utilizadas

- `csv` - Manejo de archivos CSV
- `os` - Operaciones del sistema de archivos

No se requieren dependencias externas.

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/GianePena/parcial_2_practica.git
cd parcial_2_practica
```

### 2. Verificar la estructura de carpetas

Asegúrate de que exista la siguiente estructura:

```
parcial_2_practica/
├── main.py
├── funciones_csv.py
├── utils.py
└── alumnos/
    ├── 1er_año/
    │   ├── turno_mañana/
    │   │   └── alumnos_1tm.csv
    │   └── turno_tarde/
    │       └── alumnos_1tt.csv
    ├── 2do_año/
    │   ├── turno_mañana/
    │   │   └── alumnos_2tm.csv
    │   └── turno_tarde/
    │       └── alumnos_2tt.csv
    └── 3er_año/
        ├── turno_mañana/
        │   └── alumnos_3tm.csv
        └── turno_tarde/
            └── alumnos_3tt.csv
```

### 3. Ejecutar la aplicación

```bash
python main.py
```

## 📁 Estructura del Proyecto

```
parcial_2_practica/
│
├── main.py                 # Punto de entrada - Menú principal
├── funciones_csv.py        # Operaciones CRUD sobre archivos CSV
├── utils.py                # Utilidades y validaciones
├── README.md               # Este archivo
│
└── alumnos/                # Directorio de datos
    ├── 1er_año/
    ├── 2do_año/
    └── 3er_año/
```

### Formato de archivos CSV

Cada archivo CSV tiene el siguiente formato:

```csv
nombre,apellido,ID
lucía,castro,2023-2M-001
santiago,vargas,2023-2M-002
maría,gonzález,2023-2M-003
```

### Modelo de datos

Cada alumno se representa con los siguientes atributos:

| Campo          | Tipo   | Descripción                                     |
| -------------- | ------ | ----------------------------------------------- |
| `nombre`       | String | Nombre del estudiante (en minúsculas)           |
| `apellido`     | String | Apellido del estudiante (en minúsculas)         |
| `ID`           | String | Identificador único (formato: AAAA-NX-###)      |
| `año`          | String | Año académico (extraído de la ruta del archivo) |
| `división`     | String | Turno: "mañana" o "tarde"                       |
| `ruta_archivo` | String | Ruta completa al archivo CSV correspondiente    |

## 🎮 Uso

### Menú Principal

Al ejecutar el programa, se presenta el siguiente menú:

```
--- MENU PRINCIPAL ---
1- Mostrar alumnos.
2- Mostar alumno por curso.
3- Crear alumno.
4- Editar alumno.
5- Eliminar alumno.
6- Ordenar alumnos.
7- Estadisticas alumno.
8- Salir.

Ingrese una opción:
```

### Navegación

1. Ingresa el número de la opción deseada (1-6)
2. Sigue las instrucciones en pantalla
3. El sistema validará tus entradas automáticamente
4. Presiona Enter después de cada entrada

## 🔧 Funcionalidades Detalladas

### 1️⃣ Mostrar Todos los Alumnos

Muestra un listado completo de todos los estudiantes registrados en el sistema, independientemente de su año o turno.

**Información mostrada:**

- Nombre completo
- ID único
- Año académico
- Turno (mañana/tarde)

### 2️⃣ Mostrar Alumnos por Curso

Filtra y muestra únicamente los estudiantes de un año académico específico.

**Opciones disponibles:**

- 1er año
- 2do año
- 3er año

### 3️⃣ Crear Nuevo Alumno

Permite registrar un nuevo estudiante en el sistema.

**Datos solicitados:**

1. Nombre (solo letras)
2. Apellido (solo letras)
3. Número de curso (1, 2 o 3)
4. Turno (mañana/tarde)
5. ID único (verificado contra duplicados)

**Proceso:**

- Valida todos los datos ingresados
- Verifica que el ID no exista previamente
- Crea el registro en el archivo CSV correspondiente
- Confirma la operación exitosa

### 4️⃣ Editar Alumno Existente

Modifica la información de un estudiante ya registrado.

**Proceso:**

1. Solicita el ID del alumno a editar
2. Busca el registro en todos los archivos
3. Muestra los datos actuales
4. Permite modificar nombre y/o apellido
5. Actualiza el archivo CSV correspondiente

**Nota:** El ID no puede ser modificado para mantener la integridad referencial.

### 5️⃣ Eliminar Alumno

Elimina permanentemente un registro de estudiante del sistema.

**Proceso:**

1. Solicita el ID del alumno
2. Busca y muestra los datos del alumno
3. Solicita confirmación de eliminación
4. Elimina el registro del archivo CSV
5. Confirma la operación

⚠️ **Advertencia:** Esta acción es irreversible.

### 6️⃣ Salir

Cierra la aplicación de forma segura, guardando todos los cambios realizados.

## 🏗️ Arquitectura del Código

### `main.py` - Controlador Principal

Contiene el flujo principal de la aplicación:

```python
# Bucle principal del menú
while True:
    mostrar_menu()
    opcion = input("Ingrese una opción: ")
    # Procesa la opción seleccionada
```

**Responsabilidades:**

- Gestión del menú principal
- Coordinación entre módulos
- Control del flujo de la aplicación

### `funciones_csv.py` - Operaciones CRUD

Módulo encargado de todas las operaciones sobre archivos CSV.

#### Funciones principales:

**`listar_archivos(directorio_base)`**

- Recorre recursivamente el directorio de alumnos
- Retorna lista de rutas de todos los archivos CSV
- Utiliza `os.walk()` para navegación

**`leer_datos_csv(archivos)`**

- Lee todos los archivos CSV encontrados
- Construye diccionarios de alumno con metadatos
- Retorna lista unificada de todos los estudiantes

**`filtrar_por_curso(alumnos, curso)`**

- Filtra la lista de alumnos por año académico
- Retorna sublista con estudiantes del curso especificado

**`actualizar_csv(ruta_archivo, alumnos_actualizados)`**

- Reescribe un archivo CSV con datos modificados
- Mantiene el formato y estructura original
- Maneja encoding UTF-8

**`modificar_alumno(alumnos, id_alumno)`**

- Busca el alumno por ID
- Permite editar nombre y apellido
- Actualiza el archivo CSV correspondiente

**`eliminar_alumno(alumnos, id_alumno)`**

- Localiza el registro a eliminar
- Remueve el alumno de la lista
- Actualiza el archivo CSV sin el registro eliminado

**`añadir_alumno_csv(nuevo_alumno)`**

- Agrega un nuevo registro al archivo correspondiente
- Verifica existencia del archivo
- Escribe en formato CSV correcto

### `utils.py` - Utilidades y Validaciones

Módulo con funciones auxiliares y de validación.

#### Funciones de validación:

**`validar_texto(texto, campo)`**

- Verifica que el texto no esté vacío
- Valida que contenga solo letras
- Retorna True/False según validez

**`pedir_id(mensaje, alumnos, validar_existencia=True)`**

- Solicita un ID al usuario
- Valida formato y existencia según contexto
- Previene IDs duplicados en creación
- Verifica existencia en edición/eliminación

**`buscar_por_ID(alumnos, id_buscar)`**

- Busca un alumno por su identificador
- Retorna el diccionario del alumno o None
- Búsqueda eficiente en lista de diccionarios

#### Funciones de formateo:

**`normalizar_diccionario(alumno)`**

- Prepara el diccionario para escritura CSV
- Extrae solo los campos necesarios (nombre, apellido, ID)
- Retorna diccionario normalizado

**`crear_alumno(nombre, apellido, id_alumno, curso, turno)`**

- Construye la estructura completa de un alumno
- Determina la ruta del archivo CSV correspondiente
- Retorna diccionario con todos los metadatos

#### Funciones de interfaz:

**`mostrar_alumnos(alumnos, titulo="Listado de Alumnos")`**

- Formatea e imprime lista de estudiantes
- Muestra información organizada y legible
- Incluye título personalizable

**`mostrar_menu()`**

- Imprime el menú principal de opciones
- Formato consistente y claro

## 🛡️ Validaciones y Seguridad

### Control de Entradas

✅ **Validación de texto**

- Solo se aceptan letras en nombres y apellidos
- No se permiten números o caracteres especiales
- Campos obligatorios no pueden estar vacíos

✅ **Validación de IDs**

- Verificación de unicidad en todo el sistema
- Control de formato de identificador
- Prevención de duplicados

✅ **Validación de opciones**

- Menú acepta solo números del 1 al 6
- Curso acepta solo 1, 2 o 3
- Turno acepta solo "mañana" o "tarde"

✅ **Validación de archivos**

- Verificación de existencia de archivos CSV
- Control de permisos de lectura/escritura
- Validación de estructura de directorios

### Normalización de Datos

- **Nombres y apellidos**: Convertidos automáticamente a minúsculas
- **Turnos**: Normalizados a formato estándar
- **Espacios**: Eliminados al inicio y final de textos

## ⚠️ Manejo de Errores

El sistema incluye manejo robusto de excepciones:

### Errores de Archivo

```python
try:
    # Operación con archivo
except FileNotFoundError:
    print("Error: Archivo no encontrado")
except PermissionError:
    print("Error: Sin permisos para acceder al archivo")
except IOError:
    print("Error: Error de lectura/escritura")
```

### Errores de CSV

```python
try:
    # Lectura/escritura CSV
except csv.Error:
    print("Error: Formato CSV inválido")
except UnicodeDecodeError:
    print("Error: Problema con codificación del archivo")
```

### Errores de Validación

- **ID duplicado**: "Error: El ID ya existe en el sistema"
- **ID no encontrado**: "Error: No se encontró alumno con ese ID"
- **Campo vacío**: "Error: El campo no puede estar vacío"
- **Formato inválido**: "Error: Solo se aceptan letras"

### Errores de Datos

- **Fila incompleta**: Se omite y se registra advertencia
- **Campo faltante**: Se completa con valor por defecto
- **Tipo incorrecto**: Se convierte o rechaza según contexto

## 📖 Ejemplos

### Ejemplo 1: Crear un nuevo alumno

```
--- MENU PRINCIPAL ---
1- Mostrar alumnos.
2- Mostar alumno por curso.
3- Crear alumno.
4- Editar alumno.
5- Eliminar alumno.
6- Salir.

Ingrese una opción: 3

=== CREAR NUEVO ALUMNO ===

Ingrese el nombre de alumno: María
Ingrese el apellido de alumno: González
Ingrese el número del curso (1, 2 o 3): 2
Ingrese el turno (mañana/tarde): mañana
Ingrese el ID del alumno: 2023-2M-006

✓ Alumno agregado con éxito!

Datos registrados:
- Nombre: maría gonzález
- ID: 2023-2M-006
- Curso: 2do año - Turno mañana
```

### Ejemplo 2: Listar alumnos por curso

```
Ingrese una opción: 2

Ingrese el número de curso (1, 2 o 3): 2

=== ALUMNOS DE 2DO AÑO ===

1. Lucía Castro
   ID: 2023-2M-001
   Turno: mañana

2. Santiago Vargas
   ID: 2023-2M-002
   Turno: mañana

3. María González
   ID: 2023-2M-006
   Turno: mañana

Total de alumnos: 3
```

### Ejemplo 3: Editar un alumno

```
Ingrese una opción: 4

=== EDITAR ALUMNO ===

Ingrese el ID del alumno a editar: 2023-2M-006

Alumno encontrado:
- Nombre: maría gonzález
- ID: 2023-2M-006
- Curso: 2do año - Turno mañana

Ingrese el nuevo nombre (dejar vacío para mantener): María José
Ingrese el nuevo apellido (dejar vacío para mantener):

✓ Alumno modificado exitosamente!

Datos actualizados:
- Nombre: maría josé gonzález
- ID: 2023-2M-006
```

### Ejemplo 4: Eliminar un alumno

```
Ingrese una opción: 5

=== ELIMINAR ALUMNO ===

Ingrese el ID del alumno a eliminar: 2023-2M-002

Alumno encontrado:
- Nombre: santiago vargas
- ID: 2023-2M-002
- Curso: 2do año - Turno mañana

¿Está seguro que desea eliminar este alumno? (s/n): s

✓ Alumno eliminado exitosamente!
```

## 📌 Consideraciones Importantes

### Formato de Datos

- Todos los nombres y apellidos se almacenan en **minúsculas**
- Los IDs deben ser **únicos** en todo el sistema
- El formato sugerido para IDs es: `AAAA-NX-###` (Año-Nivel-Número)

### Sincronización

- Los datos se recargan en cada iteración del menú
- Los cambios se persisten inmediatamente en los archivos CSV
- No hay caché de datos, siempre se lee del disco

### Encoding

- Todos los archivos CSV utilizan encoding **UTF-8**
- Caracteres especiales y acentos son soportados
- Compatibilidad multiplataforma (Windows, Linux, macOS)

## 👥 Autores

**Peña Gianella**  
**Fontagnol Agustina**

## Video explicativo

## https://drive.google.com/drive/folders/1ZjBvYY5ehr2HJTJajBLCrs-4QTCrOUJR?usp=sharing
