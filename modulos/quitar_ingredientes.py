def quitar_ingredientes(pedido):
    #convertir en lista el set
    ingredientes = list(pedido["ingredientes"])
    
    for i, ingr in enumerate(ingredientes , start=1):
        print(f"{i}.- {ingr}")
    
    opcion = int(input("N de ingrediente a quitar: "))

    if 1 <= opcion <= len(ingredientes):
        quitar_ingrediente = ingredientes[opcion - 1]
    else:
        print("Valor no valido")
    
    pedido["ingredientes"].remove(quitar_ingrediente)