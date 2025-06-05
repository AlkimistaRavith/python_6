

def seleccionar_masa(pedido):
    while True:
        try: 
            opcion = int(input("""Menu 1. ESCOGE LA MASA QUE PREFIERAS
selecciona la masa 
1. Masa tradicional.
2. Masa delgada.
3. Masa borde de queso.
"""))
            #opciones de masa, si se ingresa un valor erroneo, queda en bucle, se rompe con seleccion valida.
            if opcion == 1 :
                pedido["masa"] = "tradicional"
                print(f"Masa {pedido["masa"]} agregada correctamente... ")
                break
            elif opcion == 2 :
                pedido["masa"] = "delgada"
                print(f"Masa {pedido["masa"]} agregada correctamente... ")
                break
            elif opcion == 3 :
                pedido["masa"] = "borde de queso"
                print(f"Masa {pedido["masa"]} agregada correctamente... ")
                break
            else:
                #Al ingresar una opcion no disponible.
                print("La opción ingresada no es válida. Ingresa nuevamente.")
            
        #Para errores de ingresos no numericos.
        except ValueError:
            print("La opción ingresada no es válida. Ingresa nuevamente.")
        
    return pedido
