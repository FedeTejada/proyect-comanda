# Importan modulos
from menu import Menu
from compra import Compra

def main():
    menu = Menu()
    compra = Compra()
    num_compra = 1

    # Un while true para que se repita hasta que se diga lo contrario
    while True:
        # Pantalla principal con menu de opciones
        print("\n1. Mostrar Menú")
        print("2. Agregar ítem al carrito")
        print("3. Mostrar carrito")
        print("4. Calcular total")
        print("5. Confirmar compra")
        print("6. Salir\n")

        # El usuario elige la operacion que quiere realizar
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu.mostrar_menu()

        elif opcion == "2":
            item = input("\nIngrese el ítem que desea agregar: ").lower()
            cantidad = int(input("Ingrese la cantidad: "))
            compra.agregar_item(item, cantidad)
            print("Ítem agregado al carrito.")

        elif opcion == "3":
            compra.mostrar_carrito()

        elif opcion == "4":
            total = compra.calcular_total(menu)
            print(f"Total a pagar: ${total:.2f}")

        elif opcion == "5":
            cliente, hora, cadete = compra.cierre_compra()
            print("COMPRA CONFIRMADA\n")
            print(f"N° compra: {num_compra}")
            print(f"Cliente: {cliente}")
            print(f"Hora: {hora}")
            print(f"¿Cadete?: {cadete}")
            print(f"Total: ${total:.2f}")

            num_compra += 1
            # ACA HAY QUE VER COMO REINICIAR TODAS LAS VARIABLES PARA UNA PROXIMA COMPRA
            break

        elif opcion == "6":
            print("Saliendo del programa.")
            break

        # En caso de elegir una operacion incorrecta salta una advertencia y se reinicia el while
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

# Si el archivo es el main se lo llama
if __name__ == "__main__":
    main()
