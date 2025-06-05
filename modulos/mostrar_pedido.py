def mostrar_pedido(pedido):
    ingredientes = list(pedido["ingredientes"])
    print(f"""Menu 5. REVISA TU PEDIDO
Tu pedido es el siguiente:
masa: {pedido['masa']}
salsa: {pedido['salsa']}
ingredientes:""")
    for i in ingredientes:
        print(f"- {i}")