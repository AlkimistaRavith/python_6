from modulos.mostrar_pedido import mostrar_pedido

def confirmar_pedido(pedido):
    ingredientes = list(pedido["ingredientes"])
    tiempo_extra = len(ingredientes) * 2
    tiempo_espera = 20 + tiempo_extra

    confirmar = input(f"El tiempo de espera estimado es de: {tiempo_espera} minutos. \n¿Desea confirmar su pedido? (si/no): ")

    if confirmar.lower() == "si":
        print("Tu pedido se ha confirmado. \n¡Gracias por preferirnos!")
        return True  # <- Cierra el bucle desde main.py

    elif confirmar.lower() == "no":
        print("El pedido no ha sido confirmado. Puedes seguir modificándolo.")
        return False

    else:
        print("Ingreso inválido. Por favor responde con 'si' o 'no'.")
        return False
