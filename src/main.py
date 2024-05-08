# -*- coding: utf-8 -*-

from menu import Menu
from compra import Compra

def main():
    menu = Menu()
    compra = Compra()
    num_compra = 1

    while True:
        print("\n1. Mostrar Menú")
        print("2. Agregar ítem al carrito")
        print("3. Mostrar carrito")
        print("4. Calcular total")
        print("5. Confirmar compra")
        print("6. Salir\n")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu.mostrar_menu()
        elif opcion == "2":
            menu.mostrar_menu()
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
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
