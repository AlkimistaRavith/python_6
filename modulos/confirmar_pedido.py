def confirmar_pedido(pedido):
    #extraer el set de ingredientes, como lista.
    ingredientes = list(pedido["ingredientes"])
    #calculo del tiempo de espera = 20 min base + tiempo extra (2 min por largo de lista extraida)
    tiempo_extra = len(ingredientes) * 2
    tiempo_espera = 20 + tiempo_extra

    #para mantener bucle en confirmacion.
    confirmar = 0
    
    #bucle de confirmación. solo se mantiene ante ingreso de respuesta no válida.
    while confirmar == 0:
        #solicitud de confirmación
        confirmar = input(f"""Menu 6. CONFIRMAR PEDIDO
El tiempo de espera estimado es de: {tiempo_espera} minutos.
¿Desea confirmar su pedido? (si/no): """)

        #validacion de la confirmacion.
        if confirmar.lower() == "si" or confirmar.lower() == "s":
            print("Tu pedido se ha confirmado. \n¡Gracias por preferirnos!")
            return True  #Cierra el bucle desde main

        elif confirmar.lower() == "no" or confirmar.lower() == "n":
            print("El pedido no ha sido confirmado. Puedes seguir modificándolo.")
            return False #se mantiene el bucle desde main

        else:
            print("Ingreso inválido. Por favor responde con 'si' o 'no'.")
            #retornar valor a 0 para mantener en bucle
            confirmar = 0
