def mostrar_pedido(pedido):
    ingredientes = list(pedido["ingredientes"])

    print(f"""
Tu pedido es el siguiente:
masa: {pedido['masa']}
salsa: {pedido['salsa']}
ingredientes:
""")
    for i, ingr in enumerate(ingredientes , start=1):
        print(f"{i}.- {ingr}")