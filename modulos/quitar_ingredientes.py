def quitar_fruta(vaso):
    frutas = vaso["frutas"]
    print("la opciones para borrar son estas:") 
    
    for i in frutas:
        print(f"1{i}")


    opcion = int(input(": "))

    fruta = frutas[opcion]
    vaso["frutas"].remove(fruta)