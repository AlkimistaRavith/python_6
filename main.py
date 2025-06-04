from modulos.menu import menu
from modulos.crear_pedido import crear_bebida
from modulos.seleccionar_masa import seleccionar_base
from modulos.cambiar_salsa import elegir_endulzante
from modulos.agregar_ingredientes import agregar_fruta
from modulos.quitar_ingredientes import quitar_fruta


def main():
    vaso = crear_bebida()
    
    
    while True:
        menu()
        opcion = input("opcion")

        if opcion == "1":
            seleccionar_base(vaso)
            print(vaso)
             
        
        elif opcion == "2":
            elegir_endulzante(vaso)
            print(vaso)

        elif opcion == "3":
            agregar_fruta(vaso)
            print(vaso)

        elif opcion == "4":
            
            quitar_fruta(vaso)
            print(vaso)

        elif opcion == "5":
            print(vaso)
        else:
            print("salir")



if __name__ == "__main__":
    main()