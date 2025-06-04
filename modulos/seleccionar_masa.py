def seleccionar_base(vaso):
    base = ["1", "2"]
    opcion = input("""
selecciona la base 
1. para agua 
2. para leche
""")
    if opcion == base[0]:
        vaso["base"] = "agua"
        print(f"base de {vaso["base"]} agregada correctamente... ")

    elif opcion == base[1]:
        vaso["base"] = "leche"

    else:
        print("opcion no valida")  
    
    return vaso