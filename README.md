# Sistema CRUD de Gestión de Alumnos

Sistema CRUD (Create, Read, Update, Delete) para administrar datos de alumnos organizados por año y turno, utilizando archivos CSV como almacenamiento.

## Descripción

Aplicación de consola desarrollada en Python que permite gestionar información de estudiantes distribuidos en diferentes cursos y turnos. Los datos se almacenan en archivos CSV organizados jerárquicamente por carpetas.

## Estructura de Directorios

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

## Formato de Datos CSV

Cada archivo CSV contiene los siguientes campos:

```csv
nombre,apellido,ID
Lucía,Castro,2023-2M-001
Santiago,Vargas,2023-2M-002
```

### Campos del Alumno

Cada alumno contiene:
- **nombre**: String (texto)
- **apellido**: String (texto)
- **ID**: String (identificador único)
- **año**: Extraído automáticamente de la ruta del archivo
- **división**: Turno (mañana/tarde)
- **ruta_archivo**: Ubicación del CSV correspondiente

## Funcionalidades

### 1. Mostrar todos los alumnos
Lista completa de estudiantes de todos los cursos, mostrando su información completa incluyendo año y turno.

### 2. Filtrar por curso
Visualizar alumnos de un año específico (1er, 2do o 3er año), permitiendo una vista organizada por nivel académico.

### 3. Crear alumno
Agregar nuevo estudiante al sistema especificando:
- Nombre
- Apellido
- Curso (1, 2 o 3)
- Turno (mañana/tarde)
- ID único

### 4. Editar alumno
Modificar nombre o apellido de un estudiante existente. El sistema:
- Busca el alumno por ID
- Permite actualizar nombre y/o apellido
- Guarda los cambios en el archivo CSV correspondiente

### 5. Eliminar alumno
Remover estudiante del sistema de forma permanente:
- Búsqueda por ID
- Confirmación de eliminación
- Actualización automática del archivo CSV

### 6. Salir
Cerrar la aplicación de forma segura.

## Requisitos

- Python 3.10 o superior
- Módulos estándar de Python:
  - `csv`
  - `os`

## Instalación y Ejecución

1. **Clonar o descargar el proyecto**
   ```bash
   git clone https://github.com/GianePena/parcial_2_practica.git
   cd parcial_2_practica
   ```

2. **Verificar estructura de carpetas**  
   Asegúrate de que existe la carpeta `alumnos/` con la jerarquía correcta

3. **Ejecutar el programa**
   ```bash
   python main.py
   ```

## Uso

### Navegación por el menú
Selecciona una opción ingresando el número correspondiente (1-6)

```
--- MENU PRINCIPAL ---
1- Mostrar alumnos.
2- Mostar alumno por curso.
3- Crear alumno.
4- Editar alumno.
5- Eliminar alumno.
6- Salir.
```

## Estructura del Código

### Archivos principales

- **`main.py`**: Punto de entrada de la aplicación, contiene el menú principal y la lógica del programa
- **`funciones_csv.py`**: Funciones para manipulación de archivos CSV (CRUD operations)
- **`utils.py`**: Utilidades auxiliares (validaciones, búsquedas, formateo)

### Validaciones Implementadas

- ✅ Verificación de campos vacíos
- ✅ Validación de tipo de dato (solo texto para nombres/apellidos)
- ✅ Control de IDs duplicados
- ✅ Verificación de existencia de archivos
- ✅ Validación de opciones de menú
- ✅ Manejo de errores CSV

### Funciones principales (funciones_csv.py)

- **`listar_archivos()`**: Recorre recursivamente los directorios para encontrar todos los CSV
- **`leer_datos_csv()`**: Carga todos los alumnos de múltiples CSV en una lista unificada
- **`filtrar_por_curso()`**: Filtra estudiantes por año académico
- **`actualizar_csv()`**: Reescribe archivos CSV con datos modificados
- **`modificar_alumno()`**: Edita información de un estudiante
- **`eliminar_alumno()`**: Elimina un estudiante del sistema
- **`añadir_alumno_csv()`**: Crea un nuevo registro de estudiante

### Utilidades (utils.py)

- **`validar_texto()`**: Valida que el input sea texto válido
- **`pedir_id()`**: Solicita y valida ID según contexto (crear/buscar)
- **`buscar_por_ID()`**: Verifica existencia de un ID en la base de datos
- **`normalizar_diccionario()`**: Formatea datos para escritura en CSV
- **`crear_alumno()`**: Genera estructura completa de alumno
- **`mostrar_alumnos()`**: Imprime lista formateada de estudiantes
- **`mostrar_menu()`**: Despliega opciones del menú principal

## Ejemplo de Uso

```
--- MENU PRINCIPAL ---
1- Mostrar alumnos.
2- Mostar alumno por curso.
3- Crear alumno.
4- Editar alumno.
5- Eliminar alumno.
6- Salir.

Ingrese una opción: 3

Ingrese el nombre de alumno: maría
Ingrese el apellido de alumno: gonzález
Ingrese el número del curso (1, 2 o 3): 2
Ingrese el turno (mañana/tarde): mañana
Ingrese el ID del alumno: 2023-2M-006

Alumno agregado por exito!!!
```

## Consideraciones Técnicas

- Todos los nombres y apellidos se almacenan en minúsculas para mantener consistencia
- Los IDs deben ser únicos en todo el sistema
- El programa recarga los datos en cada iteración del menú para mantener sincronización con los archivos
- Los archivos CSV deben tener encoding UTF-8

## Manejo de Errores

El sistema incluye manejo de excepciones para:
- Archivos no encontrados
- Errores de lectura/escritura CSV
- Valores inválidos en inputs
- IDs duplicados o inexistentes
- Filas incompletas en CSV

## Desarrolladores

- Peña Gianella
- Fontagnol Agustina

## Información del Proyecto

- **Versión**: 1.0
- **Lenguaje**: Python 3.x
- **Tipo**: Aplicación de consola
- **Licencia**: Proyecto académico

## Contribuir

Este es un proyecto académico. Si deseas contribuir:
1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/NuevaFuncionalidad`)
3. Commit tus cambios (`git commit -m 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/NuevaFuncionalidad`)
5. Abre un Pull Request
