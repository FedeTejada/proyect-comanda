# -*- coding: utf-8 -*-

class Menu:
    def __init__(self):
        self.items = {
            "hamburguesa": 5.99, 
            "pizza": 7.99, 
            "papas fritas": 2.49, 
            "birrita": 1.50
            }

    def mostrar_menu(self):
        print("\nMenú:")
        for item, precio in self.items.items():
            print(f"{item}: ${precio}")

class Pedido:
    def __init__(self):
        self.carrito = []

    def agregar_item(self, item, cantidad):
        self.carrito.append({"item": item, "cantidad": cantidad})

    def mostrar_carrito(self):
        print("Carrito:")
        for item in self.carrito:
            print(f"{item['item']}: {item['cantidad']}")

    def calcular_total(self, menu):
        total = 0
        for item in self.carrito:
            total += menu.items.get(item['item'], 0) * item['cantidad']
        return total

    def cierre_compra(self):
        cliente = input('Nombre del cliente: ')
        hora = input('¿A qué hora le gustaría retirar la comida? ')
        cadete = input('¿Desea cadete? ')
        if cadete.lower() == "si":
            direccion = input('¿Dirección? ')
            cadete = f"Si, {direccion}"  # f-string para incluir la dirección
            return cliente, hora, cadete
        else:
            return cliente, hora, "No"

