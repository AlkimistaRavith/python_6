def mostrar_pedido(pedido):
    ingredientes = list(pedido["ingredientes"])
    print(f"""Menu 5. REVISA TU PEDIDO
Tu pedido es el siguiente:
Masa: {pedido['masa']}
Salsa: {pedido['salsa']}
Ingredientes:""")
    for i in ingredientes:
        print(f"- {i}")