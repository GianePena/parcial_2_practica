import utils



def programa_principal():
    while True:
        try:
            utils.mostrar_menu()
            opcion = int(input('Ingrese una opción: '))
            match opcion:
                case 1:
                    # mostrar_inventario(inventario)
                    pass
                case 2:
                    # inventario = agregar_instrumentos(inventario)
                    pass
                case 3:
                    # inventario = editar_instrumento(inventario)
                    pass
                case 4:
                    # inventario = eliminar_instrumento(inventario)
                    pass
                case 5:
                    # mostrar_sin_stock(inventario)
                    pass
                case 6:
                    # inventario = vender_comprar(inventario)
                    pass
                case 7:
                    # consultar_stock(inventario)
                    pass
                case 8:
                    print('Hasta luego.')
                    break
        except ValueError:
            print('Ingreso incorrecto.')
            
if __name__ == '__main__':
    programa_principal()