def cambiar_salsa(pedido):
    #dict de salsas disponibles
    salsas =  {
        1:"Tomates",
        2:"Alfredo",
        3:"Barbecue",
        4:"Pesto"
}
    #Bucle para cuando no se selecciona correctamente el tipo de salsa
    while True:
        try:
            print("Menu 2. CAMBIA LA SALSA DE TU PIZZA") 
            #Lista de las salsas para escoger.
            for k, v in salsas.items():
                print(f"{k}.- {v}")

            
            opcion = int(input("Ingresa el número de la salsa que prefieres para tu masa: "))

            if opcion in salsas:
                #Para extraer de dict, la salsa seleccionada.
                salsa = salsas[opcion]
                #Se cambia la salsa en el pedido.
                pedido["salsa"] = salsa
                print(f"Se ha cambiado tu opción a Salsa {salsa}.")
                #seleccionada la salsa, vuelve al menu principal.
                break
            else:
                #Al ingresar una opcion no disponible.
                print("La opción ingresada no es válida. Ingresa nuevamente.")
        #Para errores de ingresos no numericos.
        except ValueError:
            print("La opción ingresada no es válida. Ingresa nuevamente.")