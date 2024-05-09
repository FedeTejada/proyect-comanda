# Importan modulos
from clases.producto import Producto
from funciones import *

# Variables


# Funcion Menu
def main():

    # Un while true para que se repita hasta que se diga lo contrario
    while True:
        # Pantalla principal con menu de opciones
        print("\n¿Que desea hacer?")
        print("1 - Tomar pedido")
        print("2 - Agregar o modificar producto")
        print("3 - Reporte de ventas")
        print("4 - Salir")
        
        # El usuario elige la operacion que quiere realizar
        opcion = input("Seleccione una opción:")

        if opcion == "1":
            tomar_pedido(menu)
            return
        
        elif opcion == "2":
            return
        
        elif opcion == "3":
            return
        
        elif opcion == "4":
            print("Saliendo del programa.")
            break

        # En caso de elegir una operacion incorrecta salta una advertencia y se reinicia el while
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

# Si el archivo es el main se lo llama
if __name__ == "__main__":
    main()
