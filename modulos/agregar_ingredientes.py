def agregar_ingredientes(pedido):
    
        #dict con la lista de ingredientes para agregar.
        ingredientes =  {
            1:"Tomate", 
            2:"Champiñones",
            3:"Aceituna",
            4:"Cebolla",
            5: "Pollo",
            6: "Jamón",
            7: "Carne", 
            8: "Tocino", 
            9: "Queso"
}

        #Bucle para agregar más de un ingrediente a la vez.
        while True:
            try:
                #Muestra las opciones.
                print("Menu 3. AGREGA TUS INGREDIENTES FAVORITOS \nTenemos las siguientes opciones:") 
                for k, v in ingredientes.items():
                    print(f"{k}.- {v}")

                #Pide el ingrediente
                opcion = int(input("Escribe el número para agregar el ingrediente (o 0 para volver al menu): "))
                
                #para salir de bucle de ingredientes.
                if opcion == 0:
                    break
                elif opcion in ingredientes:
                    #extrae el ingrediente del dict.
                    ingrediente = ingredientes[opcion]
                    #agrega el ingrediente al set() del pedido
                    pedido["ingredientes"].add(ingrediente)
                    #muestra los ingredientes agregados al pedido.
                    print(f"Has agregado {pedido["ingredientes"]} a tu pedido. \nAgrega otro ingrediente.")
                else:
                    #para valores que no están listados.
                    print("La opción no está en la lista, ingresa nuevamente.")
            #Para errores de ingresos no numericos.
            except ValueError:
                print("La opción no es válida, ingresa nuevamente.")