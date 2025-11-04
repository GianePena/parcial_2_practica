def validar_texto(texto):#VALIDAR TEXTO
    try:
        if len(texto)==0:
            raise ValueError("Campo vacio, ingrese un texto")
        if texto.isdigit():
            raise ValueError("Ingrese un tipo de dato string")
        return True
    except ValueError as e:
        print("Error: ", e)
        return False

def pedir_id(alumnos, accion=None):
    while True:
        id = input("Ingrese el ID del alumno: ").strip()
        if len(id) == 0:
            print("Error: ID vacío, ingrese un ID")
            continue
        if accion == "crear":
            if buscar_por_ID(alumnos, id):
                print(f"Error: El ID '{id}' ya existe. Ingrese un ID diferente.")
                continue
            else:
                return id 
        elif accion is None:
            if not buscar_por_ID(alumnos, id):
                print(f"El alumno con ID '{id}' no existe")
                continue
            else:
                return id
    
    return id

def buscar_por_ID(alumnos, ID):#BUSCAR ALUMNO POR ID
    existe=False
    for a in alumnos:
        if a["ID"]==ID:
            existe=True
            break
    if existe:
        return True
    elif not existe:
        return False


def normalizar_diccionario(nombre, apellido, id):
    alumno_csv = {                 
        "nombre": nombre,
        "apellido": apellido,
        "ID": id
    }
    return alumno_csv

def crear_alumno(nombre, apellido, id, ruta_archivo, año, division):
    nuevo_alumno = {
        "nombre": nombre,
        "apellido": apellido,
        "ID": id,
        "ruta_archivo": ruta_archivo,
        "año": año,
        "division": division
    }
    return nuevo_alumno
def mostrar_menu():
    print('--- MENU PRINCIPAL ---')
    print('1- Mostrar alumnos.')
    print('2- Mostar alumno por curso.')
    print('3- Crear alumno.')
    print('4- Editar alumno.')
    print('5- Eliminar instrumento.')
    print('6- Salir.')


def mostrar_alumnos(alumnos):
    for a in alumnos:
        print(f"Nombre completo: {a["nombre"].capitalize()} {a["apellido"].capitalize()} || Curso: {a["año"]} || Turno: {a["division"]}")


