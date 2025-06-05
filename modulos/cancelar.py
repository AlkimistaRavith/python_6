
def cancelar_pedido(pedido):
    cancelar = input(f"Menu 0. CANCELAR PEDIDO \n¿Está seguro de cancelar su pedido? (si/no): ")

    if cancelar.lower() == "si" or cancelar.lower() == "s":
        print("Tu pedido se ha cancelado. \nvuelve pronto! Te esperamos")
        return True  # <- Cierra el bucle desde main.py

    elif cancelar.lower() == "no" or cancelar.lower() == "n":
        return False

    else:
        print("Ingreso inválido. Por favor responde con 'si' o 'no'.")
        return False