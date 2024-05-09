import sys
sys.path.append('src\clases')

from producto import Producto # Reemplaza 'archivo' con el nombre de tu archivo y 'Clase' con el nombre de tu clase o función

lomito = Producto('Lomito', 50)

hamburguesa = Producto('Hamburguesa', 100)

pizza = Producto('Pizza', 5)

empanadas = Producto('Empanadas', 100)

menu = []

def producto_nuevo(nuevo_producto: Producto):
    nombre_producto = input('Ingrese el producto a agregar: ')
    precio = int(input('¿Que precio tiene ese producto? '))
    menu.append(nuevo_producto(nombre_producto, precio))

def mostrar_producto():
    contador = 1

    for producto in menu:
        print(f'${contador} - {producto.nombre}')
        contador += 1
    
mostrar_producto()