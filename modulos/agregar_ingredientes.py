def agregar_ingredientes(pedido):
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
    print("la opciones son las siguientes :") 
    
    for k, v in ingredientes.items():
        print(f"{k}.- {v}")


    opcion = int(input(": "))

    if opcion in ingredientes:
        ingrediente = ingredientes[opcion]
        pedido["ingredientes"].add(ingrediente)