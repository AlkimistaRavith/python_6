def agregar_fruta(vaso):
    frutas =  {
        1:"manzana",
        2:"uva",
        3:"pera"
}
    print("la opciones son las siguientes :") 
    
    for k, v in frutas.items():
        print(f"{k}.- {v}")


    opcion = int(input(": "))

    if opcion in frutas:
        fruta = frutas[opcion]
        vaso["frutas"].append(fruta)