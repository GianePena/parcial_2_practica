# Sistema de Gestión de Alumnos

Trabajo Práctico - Gestión de alumnos mediante archivos CSV

## Descripción

Este programa permite gestionar información de alumnos de una institución educativa organizados por año (1°, 2° y 3°) y turno (mañana/tarde). Los datos se almacenan en archivos CSV en una estructura de directorios.

## Estructura de Archivos

```
alumnos/
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

## Archivos del Programa

- `programa_principal.py`: Archivo principal con el menú y la lógica del programa
- `funciones_csv.py`: Funciones para leer, escribir y manipular archivos CSV
- `utils.py`: Funciones auxiliares de validación y utilidades

## Formato de los CSV

Cada archivo CSV contiene:

- **nombre**: Nombre del alumno
- **apellido**: Apellido del alumno
- **ID**: Identificador único del alumno

## Menú Principal

```
--- MENU PRINCIPAL ---
1- Mostrar alumnos.
2- Mostrar alumno por curso.
3- Crear alumno.
4- Editar alumno.
5- Eliminar alumno.
6- Ordenar alumnos.
7- Estadísticas alumnos.
8- Salir.
```

## Funcionalidades

### 1. Mostrar Alumnos

Muestra todos los alumnos cargados en el sistema.

**Salida:**

```
MOSTRAR TODOS LOS ALUMNOS
Nombre completo: Juan Pérez || Curso: 1er_año || Turno: turno_mañana
Nombre completo: María González || Curso: 2do_año || Turno: turno_tarde
Nombre completo: Carlos López || Curso: 3er_año || Turno: turno_mañana
```

### 2. Mostrar Alumno por Curso

Filtra y muestra alumnos de un curso específico (1er_año, 2do_año o 3er_año).

**Entrada:**

```
Ingrese el curso por el que desea filtrar (ej: 1er_año): 1er_año
```

**Salida:**

```
FILTRAR ALUMNOS POR CURSO

--- Mostrando 5 alumno(s) ---
Nombre completo: Juan Pérez || Curso: 1er_año || Turno: turno_mañana
Nombre completo: Ana Martínez || Curso: 1er_año || Turno: turno_tarde
```

### 3. Crear Alumno

Permite agregar un nuevo alumno al sistema.

**Proceso:**

```
Ingrese el nombre de alumno: pedro
Ingrese el apellido de alumno: garcía
Ingrese el número del curso (1, 2 o 3): 2
Ingrese el turno (mañana/tarde): mañana
Ingrese el ID del alumno: 12345
Alumno agregado por exito!!!
```

El alumno se agregará automáticamente al CSV correspondiente según el curso y turno seleccionados.

### 4. Editar Alumno

Permite modificar el nombre o apellido de un alumno existente.

**Proceso:**

```
Ingrese el ID del alumno: 12345
Ingrese el campo a modificar (nombre o apellido): nombre
Ingrese el nuevo valor para nombre: pedro antonio
Alumno ID=12345 modificado con éxito.
```

### 5. Eliminar Alumno

Elimina un alumno del sistema por su ID.

**Proceso:**

```
Ingrese el ID del alumno: 12345
Alumno ID=12345 eliminado con éxito!!!
```

### 6. Ordenar Alumnos

Muestra dos tipos de ordenamiento:

#### Ordenamiento Alfabético (A-Z)

**Salida:**

```
LISTA ORDENADA DE (A-Z)
- Ana
- Carlos
- Juan
- María
- Pedro
```

#### Ordenamiento por Curso

**Salida:**

```
ORDENADOS POR CURSO:
ALUMNOS DE 1er AÑO
Nombre completo: Juan Pérez || Curso: 1er_año || Turno: turno_mañana
Nombre completo: Ana Martínez || Curso: 1er_año || Turno: turno_tarde

ALUMNOS DE 2do AÑO
Nombre completo: María González || Curso: 2do_año || Turno: turno_tarde

ALUMNOS DE 3er AÑO
Nombre completo: Carlos López || Curso: 3er_año || Turno: turno_mañana
```

### 7. Estadísticas Alumnos

Muestra estadísticas generales del sistema.

**Salida:**

```
15 ALUMNOS EN TURNO MAÑANA
Nombre completo: Juan Pérez || Curso: 1er_año || Turno: turno_mañana
Nombre completo: Carlos López || Curso: 3er_año || Turno: turno_mañana
...

10 ALUMNOS EN TURNO TARDE
Nombre completo: María González || Curso: 2do_año || Turno: turno_tarde
Nombre completo: Ana Martínez || Curso: 1er_año || Turno: turno_tarde
...

TOTAL DE ALUMNOS CARGADOS: 25
PROMEDIO DE ALUMNOS EN EL TURNO TARDE: % 40.00
PROMEDIO DE ALUMNOS EN EL TURNO MAÑANA: % 60.00
```

### 8. Salir

Finaliza el programa.

**Salida:**

```
Hasta luego.
```

## Validaciones

El programa incluye las siguientes validaciones:

- **IDs únicos**: No permite crear alumnos con IDs duplicados
- **Campos requeridos**: Verifica que todos los campos estén completos
- **Formato de texto**: Valida que nombre y apellido sean texto (no números)
- **Existencia de alumnos**: Verifica que el ID exista antes de editar o eliminar
- **Opciones del menú**: Solo acepta opciones válidas (1-8)
- **Cursos válidos**: Solo acepta 1er_año, 2do_año o 3er_año
- **Turnos válidos**: Solo acepta mañana o tarde

## Cómo Ejecutar

1. Asegúrate de tener la estructura de carpetas y archivos CSV creada
2. Ejecuta el programa principal:
   ```bash
   python programa_principal.py
   ```

## Requisitos

- Python 3.10 o superior (usa `match-case`)
- Módulos estándar: `csv`, `os`

## Notas

- Todos los nombres y apellidos se guardan en minúsculas
- Los datos se muestran con la primera letra en mayúscula
- Los cambios se guardan automáticamente en los archivos CSV correspondientes
- El programa recarga los datos en cada iteración del menú

## 👥 Autores

**Peña Gianella**  
**Fontagnol Agustina**

## Video explicativo

## https://drive.google.com/drive/folders/1ZjBvYY5ehr2HJTJajBLCrs-4QTCrOUJR?usp=sharing
