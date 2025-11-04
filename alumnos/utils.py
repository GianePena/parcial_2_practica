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

def pedir_id(alumnos):
    while True:
        id = input("Ingrese el ID del alumno: ").strip()
        if len(id) == 0:
            print("Error: ID vacío, ingrese un ID")
            continue
        if not buscar_por_ID(alumnos, id):
            print(f"El alumno con ID '{id}' no existe")
            continue
        break
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


def mostrar_menu():
    print('--- MENU PRINCIPAL ---')
    print('1- Mostrar inventario.')
    print('2- Agregar instrumentos.')
    print('3- Editar unidades.')
    print('4- Eliminar instrumento.')
    print('5- Mostrar sin stock.')
    print('6- Vender / Comprar')
    print('7- Consultar stock.')
    print('8- Salir.')