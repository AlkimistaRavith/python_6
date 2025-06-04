

def seleccionar_masa(pedido):
    try: 
        opcion = int(input("""
selecciona la masa 
1. Masa tradicional.
2. Masa delgada.
3. Masa borde de queso.
"""))
        if opcion == 1 :
            pedido["masa"] = "tradicional"
            print(f"Masa {pedido["masa"]} agregada correctamente... ")

        elif opcion == 2 :
            pedido["masa"] = "delgada"
            print(f"Masa {pedido["masa"]} agregada correctamente... ")

        elif opcion == 3 :
                pedido["masa"] = "borde de queso"
                print(f"Masa {pedido["masa"]} agregada correctamente... ")

        else:
            print("opcion no valida")
        
    
    except ValueError:
        print("opcion no valida")
    
    return pedido
