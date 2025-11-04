import csv
import os

import utils

"""
MODELO DE DATOS: SISTEMA DE ALUMNOS --> nombre=string apellido=string ID=string
JERARQUIA: 
1er año: 
  turno_mañana
      alumnos_1tm
  turno_tarde
      alumnos_1tt
2er año 
  turno_mañana
      alumnos_2tm
  turno_tarde
      alumnos_2tt
3er año
  turno_mañana
      alumnos_3tm
  turno_tarde
      alumnos_3tt
"""

ENCABEZADOS=['nombre', 'apellido', 'ID']

def listar_archivos(directorio, lista):
    """
        cargar lista de rutas de csv de alumnos
    """
    for elemento in os.listdir(directorio):
        ruta = os.path.join(directorio, elemento)
        if os.path.isdir(ruta):
            listar_archivos(ruta, lista)
        else:
            lista.append(ruta)


def leer_datos_csv(lista_rutas):#CARGAR TODOS LOS ALUMNOS DE TODOS LOS CSV EN UNA LISTA
    """
    cargar todos los alumnos de todos los csv en una sola lista de alumnos
    """
    lista = []
    for ruta in lista_rutas:
        if not ruta.endswith('.csv'):
            continue
        try: 
            with open(ruta, 'r', newline="", encoding='utf-8') as archivo:
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



def filtrar_por_curso(lista_alumnos): #MOSTAR ALUMNOS DE UN CURSO
    """
    filtar lista total de alumnos por el curso
    retorna una lista de alumnos que forman parte del mismo curso 
    """
    while True:
        curso= input("Ingrese el curso por el que desea filtrar (ej: 1er_año): ").strip().lower()
        if curso not in ["1er_año", "2do_año","3er_año"]:
            print("Error: Ingrese campo valido: 1er_año, 2do_año, 3er_año")
            continue
        break
    lista=[]
    print(f"Alumnos de {curso}")
    for alumno in lista_alumnos:
        if alumno['año']==curso:
            lista.append(alumno)
    if not lista:  # Si la lista está vacía
        print(f"No se encontraron alumnos en {curso}")
    return lista



def actualizar_csv(ruta, alumnos): #ACTUALIZAR CSV
    """
    rescribe el csv con datos modificador(eliminacion o modificacion)
    """
    with open(ruta, "w",newline="", encoding='utf-8') as archivo:
        escritor=csv.DictWriter(archivo, fieldnames=ENCABEZADOS)
        escritor.writeheader()
        escritor.writerows(alumnos)


def modificar_alumno(alumnos):
    id = utils.pedir_id(alumnos)
    for alumno in alumnos:
        if alumno["ID"] == id:
            alumno_encontrado = alumno
            break

    while True:
        campo = input("Ingrese el campo a modificar (nombre o apellido): ").strip().lower()
        if campo not in ["nombre", "apellido"]:
            print("Error: campo inválido. Solo puede modificar 'nombre' o 'apellido'.")
            continue
        break

    while True:
        nuevo_valor = input(f"Ingrese el nuevo valor para {campo}: ").strip().lower()
        if not utils.validar_texto(nuevo_valor):
            continue
        break

    alumno_encontrado[campo] = nuevo_valor
    ruta_csv = alumno_encontrado["ruta_archivo"]
    modificar_datos_ruta(alumnos, ruta_csv)
    print(f"Alumno ID={id} modificado con éxito.")


def eliminar_alumno(alumnos):
    id = utils.pedir_id(alumnos)
    alumno_encontrado = None
    for alumno in alumnos:
        if alumno["ID"] == id:
            alumno_encontrado = alumno
            break
    if not alumno_encontrado:
        print(f"No se encontró alumno con ID={id}")
        return
    alumnos.remove(alumno_encontrado)
    ruta_csv = alumno_encontrado["ruta_archivo"]
    modificar_datos_ruta(alumnos, ruta_csv)
    print(f"Alumno ID={id} eliminado con éxito!!!")



def modificar_datos_ruta(alumnos, ruta_alumno):
    alumnos_del_csv = []
    for a in alumnos:
        if a["ruta_archivo"] == ruta_alumno:
            alumno_csv = utils.normalizar_diccionario(a["nombre"], a["apellido"], a["ID"])
            alumnos_del_csv.append(alumno_csv)
    actualizar_csv(ruta_alumno, alumnos_del_csv)

def añadir_alumno_csv(alumnos):
    while True:
        nombre= input("Ingrese el nombre de alumno: ").strip().lower()
        if not utils.validar_texto(nombre):
            continue
        break
    while True:
        apellido=input("Ingrese el apellido de alumno: ").strip().lower()
        if not utils.validar_texto(apellido):
            continue
        break
    
    while True:
        curso = input("Ingrese el número del curso (1, 2 o 3): ").strip()
        if curso not in ["1", "2", "3"]:
            print("Error: Ingrese una opción válida (1, 2 o 3)")
            continue
        break
    
    while True:
        turno = input("Ingrese el turno (mañana/tarde): ").strip().lower()
        if turno not in ["mañana", "tarde"]:
            print("Error: Ingrese mañana o tarde")
            continue
        break
    while True:
        id = utils.pedir_id(alumnos, "crear")
        break
    if curso == "1" and turno == "mañana":
        ruta_archivo = "alumnos/1er_año/turno_mañana/alumnos_1tm.csv"
        año = "1er_año"
        division = "turno_mañana"
    elif curso == "1" and turno == "tarde":
        ruta_archivo = "alumnos/1er_año/turno_tarde/alumnos_1tt.csv"
        año = "1er_año"
        division = "turno_tarde"
    elif curso == "2" and turno == "mañana":
        ruta_archivo = "alumnos/2do_año/turno_mañana/alumnos_2tm.csv"
        año = "2do_año"
        division = "turno_mañana"
    elif curso == "2" and turno == "tarde":
        ruta_archivo = "alumnos/2do_año/turno_tarde/alumnos_2tt.csv"
        año = "2do_año"
        division = "turno_tarde"
    elif curso == "3" and turno == "mañana":
        ruta_archivo = "alumnos/3er_año/turno_mañana/alumnos_3tm.csv"
        año = "3er_año"
        division = "turno_mañana"
    elif curso == "3" and turno == "tarde":
        ruta_archivo = "alumnos/3er_año/turno_tarde/alumnos_3tt.csv"
        año = "3er_año"
        division = "turno_tarde"
    
    nuevo_alumno=utils.crear_alumno(nombre, apellido,id,ruta_archivo,año,division) 
    alumnos.append(nuevo_alumno)
    alumnos_del_csv = []  
    for a in alumnos:  
        if a["ruta_archivo"] == ruta_archivo:  
            alumno_csv = utils.normalizar_diccionario(a["nombre"], a["apellido"], a["ID"])
            alumnos_del_csv.append(alumno_csv)
    
    actualizar_csv(ruta_archivo, alumnos_del_csv)
    print(f"Alumno agregado por exito!!!")
