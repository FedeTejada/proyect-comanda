from clases.producto import Producto

# Variables temporales
lomito = Producto("Lomito", 100,"Sanguche")
pizza = Producto("Pizza", 200,"Pizza")
hamburguesa = Producto("Hamburguesa", 300,"Sanguche")
coca = Producto("Coca-Cola", 200,"Bebida")
cerveza = Producto("Cerveza", 50, "Bebida")

menu = [lomito, pizza, hamburguesa, coca, cerveza]

# Si el usuario quiere cargar un producto (REVISAR)


# Toma de pedidos
def tomar_pedido(menu):
    contador = 1
    total = 0
    carrito = []

    print('Que producto quiere comprar?')
    
    # Un for que recorre todos los productos en el menu y los printea
    for producto in menu:
        print(f'{contador} - {producto._nombre}')
        contador += 1
    
    # Eleccion del producto
    eleccion = int(input(''))
    
    # Siempre que el producto este dentro de la longitud del array menu el while se recorrera
    while (eleccion - 1) <= len(menu):
        indice = (eleccion - 1)
        
        # Se agrega al array carrito lo seleccionado en el menu
        carrito.append(menu[indice])
        
        longitud = len(carrito) - 1
        cantidad = int(input(f'Cuantos {carrito[longitud]._nombre}s quiere comprar? '))
        
        # Se multiplica la cantidad de ese producto con el precio que figura en el objeto
        total += (cantidad * carrito[longitud]._precio)
        
        contador = 1
        print('Algun otro producto?')
    
        for producto in menu:
            print(f'{contador} - {producto._nombre}')
            contador += 1
        eleccion = int(input(''))
        
    
    print(total)
    carrito = []



