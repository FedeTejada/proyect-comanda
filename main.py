# -*- coding: utf-8 -*-

from pedido import Pedido, Menu

def main():
    menu = Menu()
    pedido = Pedido()
    num_pedido = 1

    while True:
        print("\n1. Mostrar Menú")
        print("2. Agregar ítem al carrito")
        print("3. Mostrar carrito")
        print("4. Calcular total")
        print("5. Confirmar compra")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu.mostrar_menu()
        elif opcion == "2":
            menu.mostrar_menu()
            item = input("Ingrese el ítem que desea agregar: ").lower()
            cantidad = int(input("Ingrese la cantidad: "))
            pedido.agregar_item(item, cantidad)
            print("Ítem agregado al carrito.")
        elif opcion == "3":
            pedido.mostrar_carrito()
        elif opcion == "4":
            total = pedido.calcular_total(menu)
            print(f"Total a pagar: ${total:.2f}")
        elif opcion == "5":
            cliente, hora, cadete = pedido.cierre_compra()
            if cadete.lower() == "si":
                direccion = input("Ingrese la dirección de entrega: ")
                print(f"COMPRA CONFIRMADA\nN° Pedido: {num_pedido}\nCliente: {cliente}\nHora: {hora}\n¿Cadete?: Si\nDirección: {direccion}\nTotal: ${total:.2f}")
            else:
                print(f"COMPRA CONFIRMADA\nN° Pedido: {num_pedido}\nCliente: {cliente}\nHora: {hora}\n¿Cadete?: No\nTotal: ${total:.2f}")
            num_pedido += 1
            break
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
