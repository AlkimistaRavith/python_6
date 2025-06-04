def elegir_endulzante(vaso):

    endulzante = ["1","2"]
    opcion = input("""
selecciona los endulzantes
1. para Azucar
2. para Miel
""")
    
    if opcion == endulzante[0]:
        vaso["endulzante"] = "Azucar"
        print(f"base de {vaso["endulzante"]} agregado correctamente... ")
    elif opcion == endulzante[1]:
        vaso["endulzante"] = "Miel"
        print(f"base de {vaso["endulzante"]} agregado correctamente... ")
    else:
        print("opcion no soportada..")

    return vaso