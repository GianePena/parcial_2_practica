import csv
import os

import utils

#MODELO DE DATOS: SISTEMA DE ALUMNOS --> nombre=string apellido=string ID=string
# JERARQUIA: 
# 1er año: 
#   turno_mañana
#       alumnos_1tm
#   turno_tarde
#       alumnos_1tt
# 2er año 
#   turno_mañana
#       alumnos_2tm
#   turno_tarde
#       alumnos_2tt
# 3er año
#   turno_mañana
#       alumnos_3tm
#   turno_tarde
#       alumnos_3tt


DIRECTORIO="alumnos"
ENCABEZADOS=['nombre', 'apellido', 'ID']


#FUNCION RECURSIVA--> CARGAR RUTAS EN LA LISTA

def listar_archivos(directorio, lista):
    for elemento in os.listdir(directorio):
        ruta = os.path.join(directorio, elemento)
        if os.path.isdir(ruta):
            print(f"Directorio padre: {ruta}")
            print("--------------------------------------------")
            listar_archivos(ruta, lista)
        else:
            lista.append(ruta)
            print(ruta)


lista_rutas=[]#LISTA DE RUTA DE LOS ARCHIVOS
listar_archivos(DIRECTORIO, lista_rutas)



print(lista_rutas)#LISTA CON LAS RUTAS





def cargar_datos(lista_rutas):#CARGAR TODOS LOS ALUMNOS DE TODOS LOS CSV EN UNA LISTA
    lista = []
    for ruta in lista_rutas:
        if not ruta.endswith('.csv'):
            continue
        print(f"\nLeyendo: {ruta}")
        try: 
            with open(ruta, 'r', encoding='utf-8') as archivo:
                lector = csv.DictReader(archivo)  
                
                for fila in lector:
                    # Validar que los campos existan y no estén vacíos
                    if not fila.get("nombre") or not fila.get("apellido") or not fila.get("ID"):
                        print(f"Fila incompleta, saltando: {fila}")
                        continue
                    
                    # Limpiar y normalizar datos
                    alumno = {
                        "nombre": fila["nombre"].strip().lower(),
                        "apellido": fila["apellido"].strip().lower(),
                        "ID": fila["ID"].strip(),
                        "ruta_archivo": ruta 
                    }
                    
                    # Extraer jerarquía del path
                    partes_ruta = ruta.split(os.sep)
                    if len(partes_ruta) >= 2:
                        alumno['año'] = partes_ruta[1] if len(partes_ruta) > 1 else ''
                        if len(partes_ruta) >= 3:
                            alumno['division'] = partes_ruta[2] if len(partes_ruta) > 2 else ''
                    
                    lista.append(alumno)
                    
        except FileNotFoundError:
            print(f'Error: Archivo no encontrado - {ruta}')
        except csv.Error as e:
            print(f'Error al leer CSV {ruta}: {e}')
        except Exception as e:
            print(f'Error inesperado con {ruta}: {e}')
    
    return lista
cargar_datos(lista_rutas)


alumnos=cargar_datos(lista_rutas)#LISTADO DE TODOS LOS ALUMNOS


def mostrar_items_ruta(lista_alumnos, ruta_csv):#MOSTRAR TODOS LOS ALUMNOS DE UN RUTA
    lista=[]
    print(f"Alumnos en {ruta_csv}:")
    for alumno in lista_alumnos:
        if alumno['ruta_archivo']==ruta_csv:
            lista.append(alumno)
            print("-",alumno["nombre"].capitalize(), alumno["apellido"].capitalize())

#mostrar_items_ruta(alumnos,'alumnos/3er_año/turno_tarde/alumnos_3tt.csv')


def filtrar_por_curso(lista_alumnos, curso): #MOSTAR ALUMNOS DE UN CURSO
    lista=[]
    print(f"Alumnos de {curso}")
    for alumno in lista_alumnos:
        if alumno['año']==curso:
            lista.append(alumno)
            print("-",alumno["nombre"].capitalize(), alumno["apellido"].capitalize())
# filtrar_por_curso(alumnos,"3er_año")



def actualizar_csv(ruta, alumnos): #ACTUALIZAR CSV
    with open(ruta, "w",newline="") as archivo:
        escritor=csv.DictWriter(archivo, fieldnames=ENCABEZADOS)
        escritor.writeheader()
        escritor.writerows(alumnos)

def modificar_alumno(alumnos):#ACTUALIZAR CAMPO DEL CSV 
    id=utils.pedir_id(alumnos)
    while True:
        valor_a_modificar= input("Ingrese el nombre del campo a modificar: ").strip().lower()
        if valor_a_modificar not in ["nombre", "apellido"]:
            print("Error: Ingrese campo valido: nombre o apellido")
            continue
        break
    while True:
        nuevo_valor=input("Ingrese el nuevo valor:  ").strip().lower()
        if not utils.validar_texto(nuevo_valor):
            continue
        break
    for alumno in alumnos:
        if alumno["ID"] == id:
            alumno[valor_a_modificar] = nuevo_valor
            ruta_csv = alumno["ruta_archivo"]
            break
    alumnos_del_csv = []  
    for a in alumnos:  # BUSCAR MODIFICAR SOLO LOS ARCHIVOS DE SA RUTA
        if a["ruta_archivo"] == ruta_csv:  
            alumno_csv = utils.normalizar_diccionario(a["nombre"],a["apellido"],a["ID"])
            alumnos_del_csv.append(alumno_csv) 
    actualizar_csv(ruta_csv, alumnos_del_csv)#ACTUALIZAR CSV
    print(f"Alumno ID={id} modificado")


def eliminar_alumno(alumnos):
    id=utils.pedir_id(alumnos)
    for alumno in alumnos:
        if alumno["ID"] == id:
            alumnos.remove(alumno)
            ruta_csv = alumno["ruta_archivo"]
            break
    alumnos_del_csv = []  
    for a in alumnos:  # BUSCAR MODIFICAR SOLO LOS ARCHIVOS DE SA RUTA
        if a["ruta_archivo"] == ruta_csv:  
            alumno_csv = utils.normalizar_diccionario(a["nombre"],a["apellido"],a["ID"])
            alumnos_del_csv.append(alumno_csv) 
        actualizar_csv(ruta_csv, alumnos_del_csv)
    print(f"Alumno ID={id} eliminado con exito!!!")

eliminar_alumno(alumnos)




def cargar_datos_csv(alumnos):
    while True:
        nombre= input("Ingrese el nombre de alumno: ").strip().lower()
        if not utils.validar_texto(nombre):
            continue
        break
    while True:
        apellido=input("Ingrese el apelido de alumno: ").strip().lower()
        if not utils.validar_texto(apellido):
            continue
        break
    id=utils.pedir_id(alumnos)
    if "1M" in id:
        ruta_archivo="alumnos/1er_año/turno_mañana/alumnos_1tm.csv"
    elif "1T" in id:
        ruta_archivo="alumnos/1er_año/turno_tarde/alumnos_1tt.csv"
    elif "2M" in id:
        ruta_archivo="alumnos/2do_año/turno_mañana/alumnos_2tm.csv"
    elif "2T" in id:
        ruta_archivo="alumnos/2do_año/turno_tarde/alumnos_2tt.csv"
    elif "3M" in id:
        ruta_archivo="alumnos/3er_año/turno_tarde/alumnos_3tt.csv"
    elif "3T" in id:
        ruta_archivo="alumnos/3er_año/turno_mañana/alumnos_3tm.csv"
    alumnos.append(nuevo_alumno)
    nuevo_alumno=utils.normalizar_diccionario(nombre, apellido, id)
    for alumno in alumnos:
        if alumno["ID"] == id:
            alumnos.remove(alumno)
            ruta_csv = alumno["ruta_archivo"]
            break
    alumnos_del_csv = []  
    for a in alumnos:  
        if a["ruta_archivo"] == ruta_csv:  
            alumno_csv = utils.normalizar_diccionario(a["nombre"],a["apellido"],a["ID"])
            alumnos_del_csv.append(alumno_csv) 
        actualizar_csv(ruta_csv, alumnos_del_csv)
    print(f"Alumno ID={id} eliminado con exito!!!")


rutas = [{"año": "1ro",
         "turno":"tarde"
          "ruta":"" }








# def inicializar_archivo(ruta):
#     if not os.path.exists(ruta):
#         with open(ruta, 'w', newline='', encoding='utf-8') as archivo:
#             escritor = csv.DictWriter(archivo, fieldnames=ENCABEZADOS)
#             escritor.writeheader()

# def actualizar_datos(ruta, lista):
#     with open(ruta, 'w', newline='', encoding='utf-8') as archivo:
#         escritor = csv.DictWriter(archivo, fieldnames=ENCABEZADOS)
#         escritor.writeheader()
#         escritor.writerows(lista)

# def mostrar_menu():
#     print('--- MENU PRINCIPAL ---')
#     print('1- Mostrar inventario.')
#     print('2- Agregar instrumentos.')
#     print('3- Editar unidades.')
#     print('4- Eliminar instrumento.')
#     print('5- Mostrar sin stock.')
#     print('6- Vender / Comprar')
#     print('7- Consultar stock.')
#     print('8- Salir.')
    
# def mostrar_inventario(lista):
#     if not lista:
#         print('No hay instrumentos disponibles.')
#     else:
#         for elem in lista:
#             print(f'- {elem['instrumento'].capitalize()} - {elem['unidades']} unidades.')

# def agregar_instrumentos(lista):
#     try:
#         cant_inst = int(input('Cuantos instrumentos quiere agregar? '))
#         for i in range(cant_inst):
#             nombre = input(f'Nombre del instrumento {i+1}: ').lower().strip()
#             while True:
#                 cant = input('Cantidad de unidades: ')
#                 if cant.isdigit():
#                     cant = int(cant)
#                     break
#             lista.append({'instrumento':nombre, 'unidades':cant})
#         actualizar_datos(lista)
#         return lista
#     except ValueError:
#         print('Debés ingresar un número entero.')

# def editar_instrumento(inventario):
#     instrumento = input('Ingrese el nombre del instrumento que quiere editar: ').lower().strip()
#     for elem in inventario:
#         if(instrumento == elem['instrumento']):
#             while True:
#                 try:
#                     unid = int(input('Ingrese las unidades del instrumento: '))
#                     elem['unidades'] = unid
#                     actualizar_datos(inventario)
#                     return inventario
#                 except ValueError:
#                     print('Ingrese un número entero.')

# def eliminar_instrumento(inventario):
#     lista_nva = []
#     instrumento = input('Ingrese el nombre del instrumento que quiere eliminar: ').lower().strip()
#     for elem in inventario:
#         if(instrumento == elem['instrumento']):
#             continue
#         lista_nva.append(elem)
#     actualizar_datos(lista_nva)
#     return lista_nva

# def mostrar_sin_stock(inventario):
#     for elem in inventario:
#         if(elem['unidades'] == 0):
#             print(f'- {elem['instrumento']}')

# def vender_comprar(inventario):
#     inst = input('Que instrumento quiere vender o comprar? ').lower().strip()
#     for elem in inventario:
#         if(inst == elem['instrumento']):
#             opcion_vc = input('Querés vender o comprar? (v/c): ').lower().strip()
#             match opcion_vc:
#                 case 'v':
#                     if(elem['unidades'] == 0):
#                         print('No hay unidades disponibles')
#                     else:
#                         try:
#                             cant = int(input('Cuantas unidades va a vender? '))
#                             if(elem['unidades'] < cant):
#                                 print('No hay unidades disponibles.')
#                             else:
#                                 elem['unidades'] -= cant
#                                 print('Unidades vendidas.')
#                                 actualizar_datos(inventario)
#                                 return inventario
#                         except ValueError:
#                             print('Las unidades son números enteros.')
#                 case 'c':
#                     try:
#                         cant = int(input('Cuantas unidades va a comprar? '))
#                         elem['unidades'] += cant
#                         print('Unidades agregadas.')
#                         actualizar_datos(inventario)
#                         return inventario
#                     except ValueError:
#                         print('Las unidades son números enteros.')
#                 case _:
#                     print('Opcion incorrecta.')
#                     return inventario

# def consultar_stock(inventario):
#     if not inventario:
#         print('No hay instrumentos disponibles.')
#     else:
#         instrumento = input('Ingrese el nombre del instrumento que quiere consultar: ').lower().strip()
#         for elem in inventario:
#             if instrumento == elem['instrumento']:
#                 print(f'{elem['unidades']} unidades disponibles.')
#             else:
#                 print('No existe ese instrumento.')
