class Compra:
    # La funcion principal es crear un array vacio
    def __init__(self):
        self.carrito = []

    # Al array vacio se le suman los items que se elijan
    def agregar_item(self, item, cantidad):
        self.carrito.append({"item": item, "cantidad": cantidad})

    def mostrar_carrito(self):
        print("Carrito:")
        for item in self.carrito:
            print(f"{item['item']}: {item['cantidad']}")

    def calcular_total(self, menu):
        total = 0
        # Un for por cada item que multiplicara el producto por la cantidad y se sumara al total
        for item in self.carrito:
            total += menu.items.get(item['item'], 0) * item['cantidad']
        return total

    def cierre_compra(self):
        cliente = input('Nombre del cliente: ')
        hora = input('¿A qué hora le gustaría retirar la comida? ')
        cadete = input('¿Desea cadete? ')
        # Si desea cadete se correra un if que modifique la variable cadete
        if cadete.lower() == 'si':
            cadete = 'Si, a ' + input('¿A qué direccion? ')
        return cliente, hora, cadete
