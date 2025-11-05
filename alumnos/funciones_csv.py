import csv
import os

import utils


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
                            alumno['turno'] = partes_ruta[2] if len(partes_ruta) > 2 else ''
                    
                    lista.append(alumno)
                    
        except FileNotFoundError:
            print(f'Error: Archivo no encontrado - {ruta}')
        except csv.Error as e:
            print(f'Error al leer CSV {ruta}: {e}')
        except Exception as e:
            print(f'Error inesperado con {ruta}: {e}')
    
    return lista

def filtrar_alumnos(lista_alumnos, dato_ingresado, campo_a_modif): #MOSTAR ALUMNOS DE UN CURSO
    """
    dato ingresado: dato que correcponde al campo por el se quiere filtar (dato=mañana, 1er_año)
    campo a modificar: turno, año
    filtar lista total de alumnos por el curso
    retorna una lista de alumnos que forman parte del mismo curso 
    """

    lista=[]
    for alumno in lista_alumnos:
        if alumno[campo_a_modif]==dato_ingresado:
            lista.append(alumno)
    if not lista:  # Si la lista está vacía
        print(f"No se encontraron alumnos en {dato_ingresado}")
    return lista

def pedir_curso():
    while True:
        curso= input("Ingrese el curso por el que desea filtrar (ej: 1er_año): ").strip().lower()
        if curso not in ["1er_año", "2do_año","3er_año"]:
            print("Error: Ingrese campo valido: 1er_año, 2do_año, 3er_año")
            continue
        return curso


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
        turno = "turno_mañana"
    elif curso == "1" and turno == "tarde":
        ruta_archivo = "alumnos/1er_año/turno_tarde/alumnos_1tt.csv"
        año = "1er_año"
        turno = "turno_tarde"
    elif curso == "2" and turno == "mañana":
        ruta_archivo = "alumnos/2do_año/turno_mañana/alumnos_2tm.csv"
        año = "2do_año"
        turno = "turno_mañana"
    elif curso == "2" and turno == "tarde":
        ruta_archivo = "alumnos/2do_año/turno_tarde/alumnos_2tt.csv"
        año = "2do_año"
        turno = "turno_tarde"
    elif curso == "3" and turno == "mañana":
        ruta_archivo = "alumnos/3er_año/turno_mañana/alumnos_3tm.csv"
        año = "3er_año"
        turno = "turno_mañana"
    elif curso == "3" and turno == "tarde":
        ruta_archivo = "alumnos/3er_año/turno_tarde/alumnos_3tt.csv"
        año = "3er_año"
        turno = "turno_tarde"
    
    nuevo_alumno=utils.crear_alumno(nombre, apellido,id,ruta_archivo,año,turno) 
    alumnos.append(nuevo_alumno)
    alumnos_del_csv = []  
    for a in alumnos:  
        if a["ruta_archivo"] == ruta_archivo:  
            alumno_csv = utils.normalizar_diccionario(a["nombre"], a["apellido"], a["ID"])
            alumnos_del_csv.append(alumno_csv)
    
    actualizar_csv(ruta_archivo, alumnos_del_csv)
    print(f"Alumno agregado por exito!!!")



def ordenar_por_nombre(alumnos):
    lista_nombre = alumnos.copy() 
    lista_nombre.sort(key=lambda x: x["nombre"])
    return lista_nombre

def ordenar_por_curso(alumnos):
    alumnos_1er_año=[]
    alumnos_2do_año=[]
    alumnos_3er_año=[]
    for a in alumnos:
        if a["año"]=="1er_año":
            alumnos_1er_año.append(a)
        elif a["año"]=="2do_año":
            alumnos_2do_año.append(a)
        elif a["año"]=="3er_año":
            alumnos_3er_año.append(a)
    return alumnos_1er_año, alumnos_2do_año, alumnos_3er_año



def mostrar_estadisticas(alumnos):
    
    alumnos_mañana=filtrar_alumnos(alumnos,"turno_mañana","turno")
    print(f"{len(alumnos_mañana)} ALUMNOS EN TURNO MAÑANA")
    utils.mostrar_alumnos(alumnos_mañana)
    
    alumnos_tarde=filtrar_alumnos(alumnos,"turno_tarde","turno")
    print(f"{len(alumnos_tarde)} ALUMNOS EN TURNO TARDE")
    utils.mostrar_alumnos(alumnos_tarde)

    print(f"TOTAL DE ALUMNOS CARGADOS: {len(alumnos)}")
    promedio_tarde, promedio_mañana=promedio_por_turno(alumnos)
    print (f"PROMEDIO DE ALUMNOS EN EL TURNO TARDE:  {promedio_tarde*100:.2f}% ")
    print (f"PROMEDIO DE ALUMNOS EN EL TURNO MAÑANA: {promedio_mañana*100:.2f}% ")
    

def promedio_por_turno(alumnos):
    cantidad_tarde=0
    cantidad_mañana=0
    for a in alumnos:
        if a["turno"]=="turno_mañana":
            cantidad_mañana+=1
        elif a["turno"]=="turno_tarde":
            cantidad_tarde+=1
    promedio_tarde=cantidad_tarde/len(alumnos)
    promedio_mañana=cantidad_mañana/len(alumnos)
    return promedio_tarde, promedio_mañana

