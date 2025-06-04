def cambiar_salsa(pedido):
    try:
        salsas =  {
            1:"Tomates",
            2:"Alfredo",
            3:"Barbecue",
            4:"Pesto"
}
        print("Elige la salsa que prefieres:") 
        
        for k, v in salsas.items():
            print(f"{k}.- {v}")

        opcion = int(input(": "))

        if opcion in salsas:
            salsa = salsas[opcion]
            pedido["salsa"] = salsa
        else:
            print("opcion no valida")
    
    except ValueError:
        print("opcion no valida")