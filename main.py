from modulos.menu import menu
from modulos.crear_pedido import crear_pedido
from modulos.seleccionar_masa import seleccionar_masa
from modulos.cambiar_salsa import elegir_endulzante
from modulos.agregar_ingredientes import agregar_fruta
from modulos.quitar_ingredientes import quitar_fruta


def main():
    pedido = crear_pedido()
    print("""
    ----    BIENBENIDO A PIZZA JAT  ----
Disfruta de un momento innolvidable, prefiere nuestras pizzas.
¿Qué deseas pedir?
""")
    
    while True:
        menu()
        opcion = input("opcion")

        if opcion == "1":
            seleccionar_masa(pedido)
            print(pedido)
             
        
        elif opcion == "2":
            elegir_endulzante(pedido)
            print(pedido)

        elif opcion == "3":
            agregar_fruta(pedido)
            print(pedido)

        elif opcion == "4":
            
            quitar_fruta(pedido)
            print(pedido)

        elif opcion == "5":
            print(pedido)
        elif opcion == "6":
            print("gracias por su seleccion <agregar>")
            break



if __name__ == "__main__":
    main()