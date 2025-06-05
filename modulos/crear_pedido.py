def crear_pedido():
    #dict de la variable a trabajar.
    pedido = {
        "masa":"Tradicional", #por defecto masa tradicional
        "salsa":"Tomates", #por defecto salsa de tomates
        "ingredientes": set() #Se define un set(), para no repetir ingredientes.
    }
    return pedido