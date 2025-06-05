def mostrar_pedido(pedido):
    #Obtener lista de ingredientes del set() en el dict pedido
    ingredientes = list(pedido["ingredientes"])
    #Imprime pociones de masa y salsa.
    print(f"""Menu 5. REVISA TU PEDIDO
Tu pedido es el siguiente:
Masa: {pedido['masa']}
Salsa: {pedido['salsa']}
Ingredientes:""")
    #Imprime lista de ingredientes.
    for i in ingredientes:
        print(f"- {i}")