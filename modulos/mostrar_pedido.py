def mostrar_pedido(pedido):
    ingredientes = list(pedido["ingredientes"])
    tiempo_extra = len(ingredientes) * 2
    tiempo_espera = 20 + tiempo_extra

    print(f"""
Tu pedido es el siguiente:
masa: {pedido['masa']}
salsa: {pedido['salsa']}
ingredientes:
""")
    for i, ingr in enumerate(ingredientes , start=1):
        print(f"{i}.- {ingr}")

    print(f"\nEl tiempo de espera será de: {tiempo_espera} minutos.")