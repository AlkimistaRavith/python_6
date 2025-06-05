def quitar_ingredientes(pedido):
    #convertir en lista el set
    ingredientes = list(pedido["ingredientes"])
    
    if ingredientes == []:
        print("Menu 4. QUITAR INGREDIENTES \nAun no tienes ingredientes agregados.")
    else:
        #Enumerar la lista, partiendo de 1.
        for i, ingr in enumerate(ingredientes , start=1):
            print(f"{i}.- {ingr}")
        
        opcion = int(input("Ingresa el número del ingrediente que deseas quitar: "))

        #Condicional para evaluar que la opción está dentro de la lista.
        if 1 <= opcion <= len(ingredientes):
            #obtiene el ingrediente de la lista numerada.
            quitar_ingrediente = ingredientes[opcion - 1]
        else:
            print("Valor no valido")
        
        #Elimina elemento del set() en el pedido.
        pedido["ingredientes"].remove(quitar_ingrediente)