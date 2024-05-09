from product import Product
##Creo los productos que tiene para vender la carta
##Inicializamos en 0 la cantidad para que se vaya agregando mientras se hace un pedido.
lomito = Product("Lomo",0,15)
hamburgesa = Product("Hamburguesa",0,10)
mila = Product("Sandwich de milanesa",0,13)
## FUNCIONES PARA TRABAJAR 
carrito = []

def menu():
    while(True):  
        print("1- Lomito")
        print("2- Hamburguesa")
        print("3- Sandwich de mila")
        print("4- Totla")
        print("5- Mostrar pedido")
        print("6- Cambiar precio a los productos")
        print("7- Salir")
        opcion = input("\nIngrese una opcion: ")
        print(opcion)
        if (opcion == "1"):
            agregarProductosCarrito(lomito)
        elif(opcion == "2"):
            agregarProductosCarrito(hamburgesa)
        elif(opcion == "3"):
            agregarProductosCarrito(mila)
        elif(opcion == "5"):
            mostrarPedido(carrito)
        elif(opcion == "7"):
            print("Cerrando")
            break
        else:
            print("Opcion no valida ingrese una opcion correcta\n")

## Agregar al pedido, cada vez que se agregue la funcion deveria pushearlo al arreglo y aumentar la cantidad del objeto
## Ver como validar para que la funcion haga lo que queremos y tratar el error que se pueda ocurrir.
def agregarProductosCarrito(product:object):
    carrito.append(product)

##Mostrar el pedido, que podemos hacerlo para que imprima hay que darle el diseño que quiere pleita
def mostrarPedido(cart:object):
    for car in cart:
        print("Pedido: ")
        print(f"Nombre: {car._name} Cantidad: {car._cant} Precio {car._price}")


##Calcular el total del carrito, comprobar que devuelva el valor bien echo. Y validar si hace falta. 
def calculateTotal(cart:object):
    total = 0
    for carr in cart:
        total += carr._cant * carr._price
    return total

##Desarrollar las funciones que esten faltando para complementar el programa. Analizaro con gino.