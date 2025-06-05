def quitar_ingredientes(pedido):
    #convertir en lista el set
    ingredientes = list(pedido["ingredientes"])
    
    #en caso que no existan elementos para quitar.
    if ingredientes == []:
        print("Menu 4. QUITAR INGREDIENTES \nAun no tienes ingredientes agregados.")
    #Para iniciar menu 4.
    else:
        try:
            #Enumerar la lista, partiendo de 1.
            for i, ingr in enumerate(ingredientes , start=1):
                print(f"{i}.- {ingr}")
            
            opcion = int(input("Ingresa el número del ingrediente que deseas quitar: "))

            #Condicional para evaluar que la opción está dentro de la lista.
            if 1 <= opcion <= len(ingredientes):
                #obtiene el ingrediente de la lista numerada.
                quitar_ingrediente = ingredientes[opcion - 1]
            else:
                #Solo da la advertencia y retorna al menu (la pizzeria no quiere que se reduzca el pedido)
                print("La opción no está en la lista. Debe ser un número de la lista")
            
            #Elimina elemento del set() en el pedido.
            pedido["ingredientes"].remove(quitar_ingrediente)
        #Para errores de ingresos no numericos.
        except ValueError:
            print("La opción ingresada no es válida. Debe ser un número de la lista.")