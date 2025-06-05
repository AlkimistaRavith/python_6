from modulos.menu import menu
from modulos.crear_pedido import crear_pedido
from modulos.seleccionar_masa import seleccionar_masa
from modulos.cambiar_salsa import cambiar_salsa
from modulos.agregar_ingredientes import agregar_ingredientes
from modulos.quitar_ingredientes import quitar_ingredientes
from modulos.mostrar_pedido import mostrar_pedido
from modulos.confirmar_pedido import confirmar_pedido


def main():
    #función para crear el diccionario con el pedido.
    pedido = crear_pedido()
    #Mensaje de entrada al programa.
    print("""
    ----    BIENBENIDO A PIZZA JAT  ----
Disfruta de un momento innolvidable, prefiere nuestras pizzas.
¿Qué deseas pedir?
""")
    
    while True:
        #Se muestra el menu (se mostrará mientras se este armando pedido.)
        menu()
        opcion = input("opcion")

        if opcion == "1":
            #función para escojer 1er elemento de dict (masa)
            seleccionar_masa(pedido)
            print(pedido)
             
        
        elif opcion == "2":
            #función para escojer 3do elemento de dict (salsa)
            cambiar_salsa(pedido)
            print(pedido)

        elif opcion == "3":
            #función para agregar ingredientes al pedido (ingredientes)
            agregar_ingredientes(pedido)
            print(pedido)

        elif opcion == "4":
            #funcion para eliminar ingredientes del pedido.
            quitar_ingredientes(pedido)
            print(pedido)

        elif opcion == "5":
            #funcion para listar el pedido.
            mostrar_pedido(pedido)
        
        elif opcion == "6":
            #funcion para listar el pedido y mostrar el tiempo de espera estimado.
            mostrar_pedido(pedido)
            #para confirmar o cancelar pedido
            if confirmar_pedido(pedido):
                break



if __name__ == "__main__":
    main()