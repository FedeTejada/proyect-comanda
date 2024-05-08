class Menu:
    # Llamo a la funcion principal de la clase donde se van a cargar los items
    def __init__(self):
        self.items = {
            "hamburguesa": 5.99, 
            "pizza": 7.99, 
            "papas fritas": 2.49, 
            "birrita": 1.50
            }

    # Recorro un for por cada producto en el menu y lo imprimo.
    def mostrar_menu(self):
        print("\nMenú:")
        for item, precio in self.items.items():
            print(f"{item}: ${precio}")
