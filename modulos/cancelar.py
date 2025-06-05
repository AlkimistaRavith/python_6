
def cancelar_pedido(pedido):
    #valor para entrar en bucle interno.
    cancelar = 0

    #bucle para casos de ingreso de respuesta erroneo (distinto a si/no/s/n)
    while cancelar == 0:
        #para validar la cancelación
        cancelar = input(f"Menu 0. CANCELAR PEDIDO \n¿Está seguro de cancelar su pedido? (si/no): ")

        #validacion de la cancelación
        if cancelar.lower() == "si" or cancelar.lower() == "s":
            print("Tu pedido se ha cancelado. \nvuelve pronto! Te esperamos")
            return True  #Cierra el bucle desde main

        elif cancelar.lower() == "no" or cancelar.lower() == "n":
            return False #Continua el bucle de menu en main

        else:
            print("Ingreso inválido. Por favor responde con 'si' o 'no'.")
            #para mentener el bucle en cancelar hasta tener respuesta valida.
            cancelar = 0