# -*- coding: utf-8 -*-



class Compra:
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
        return cliente, hora, cadete

