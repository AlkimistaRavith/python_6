from modulos.menu import menu
from modulos.crear_pedido import crear_pedido
from modulos.seleccionar_masa import seleccionar_masa
from modulos.cambiar_salsa import cambiar_salsa
from modulos.agregar_ingredientes import agregar_ingredientes
from modulos.quitar_ingredientes import quitar_ingredientes


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
            #para mostrar el pedido - FALTA PRESENTA MEJOR EL PEDIDO Y ESTIMAR TIEMPO DE PREPARACION
            print(pedido)
        elif opcion == "6":
            #para finalizar - MODIFICAR EN UNA FUNCIÓN PARA PREGUNTAR SI SE PIDE O SE CANCELA.
            print("gracias por su seleccion <agregar>")
            break



if __name__ == "__main__":
    main()