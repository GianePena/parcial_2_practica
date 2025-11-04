import utils
import funciones_csv as csv

DIRECTORIO="alumnos"

lista_rutas=[]#LISTA DE RUTA DE LOS ARCHIVOS
csv.listar_archivos(DIRECTORIO, lista_rutas)

def programa_principal():
    while True:
        alumnos=csv.leer_datos_csv(lista_rutas)
        try:
            utils.mostrar_menu()
            opcion = int(input('Ingrese una opción: '))
            match opcion:
                case 1:#mostar alumno
                    print("MOSTAR TODOS LOS ALUMNOS")
                    utils.mostrar_alumnos(alumnos)
                case 2:#filtrar alumno por curso
                    print("FILTRAR ALUMNOS POR CURSO")
                    alumnos_filtrados = csv.filtrar_por_curso(alumnos)
                    if alumnos_filtrados: 
                        print(f"\n--- Mostrando {len(alumnos_filtrados)} alumno(s) ---")
                        utils.mostrar_alumnos(alumnos_filtrados)
                    else:
                        print("No hay alumnos para mostrar")
                case 3:#crear alumno
                    csv.añadir_alumno_csv(alumnos)
                    pass
                case 4:#editar alumno 
                    csv.modificar_alumno(alumnos) 
                    pass
                case 5:#eliminar alumno
                    csv.eliminar_alumno(alumnos)
                case 6: 
                    print('Hasta luego.')
                    break
                case _:
                    print('Error: Ingrese una opcion valida entre 1 y 6.')
                    continue
        except ValueError:
            print('Ingreso incorrecto.')
            
if __name__ == '__main__':
    programa_principal()