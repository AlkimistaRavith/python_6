from modulos.menu import menu
from modulos.crear_pedido import crear_pedido
from modulos.seleccionar_masa import seleccionar_masa
from modulos.cambiar_salsa import cambiar_salsa
from modulos.agregar_ingredientes import agregar_ingredientes
from modulos.quitar_ingredientes import quitar_ingredientes
from modulos.mostrar_pedido import mostrar_pedido
from modulos.confirmar_pedido import confirmar_pedido
from modulos.cancelar import cancelar_pedido


def main():
    #función para crear el diccionario con el pedido.
    pedido = crear_pedido()
    #Mensaje de entrada al programa.
    print("""    ----    BIENBENIDO A PIZZA JAT  ----
Disfruta de un momento innolvidable, prefiere nuestras pizzas.
Comencemos a armar tu pizza!""")
    
    while True:
        #Se muestra el menu
        print("\n¿Qué quieres hacer?")
        menu()
        opcion = input("Ingresa el número para acceder al menú: ")
        print("""
""")

        if opcion == "1":
            #función para escojer 1er elemento de dict (masa)
            seleccionar_masa(pedido)             
        
        elif opcion == "2":
            #función para escojer 3do elemento de dict (salsa)
            cambiar_salsa(pedido)

        elif opcion == "3":
            #función para agregar ingredientes al pedido (ingredientes)
            agregar_ingredientes(pedido)

        elif opcion == "4":
            #funcion para eliminar ingredientes del pedido.
            quitar_ingredientes(pedido)

        elif opcion == "5":
            #funcion para listar el pedido.
            mostrar_pedido(pedido)
        
        elif opcion == "6":
            #Primero se gatilla opcion 5 automnaticamente, para revisar ingredientes.
            mostrar_pedido(pedido)
            #Para confirmar o para volver al menu
            if confirmar_pedido(pedido):
                break

        elif opcion == "0":
            #Para cancelar pedido, sin confirmar.
            if cancelar_pedido(pedido):
                break

        else:
            print("Tu selección no es válida. Recuerda ingresar el número del menú al que deseas acceder.")



if __name__ == "__main__":
    main()