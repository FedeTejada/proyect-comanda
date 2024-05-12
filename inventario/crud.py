from clases.producto import Producto
lomito = Producto("Lomito", 100,"Sanguche")
pizza = Producto("Pizza", 200,"Pizza")
hamburguesa = Producto("Hamburguesa", 300,"Sanguche")
coca = Producto("Coca-Cola", 200,"Bebida")
cerveza = Producto("Cerveza", 50, "Bebida")

menu = [lomito, pizza, hamburguesa, coca, cerveza]
categoria = ["Sanguche", "Pizza", "Bebida"]

def AgregarNuevoProducto(menu):
    nombre_producto = input('Ingrese el nombre del producto: ')
    precio = int(input('¿Que precio tiene ese producto? '))
    i = 1
    print("Elija la categoria")
    for elem in categoria:
        print(f"{i}-",elem)
        i += 1
    print(f"{len(categoria)}","Salir")
    cat = int(input(""))
    if(cat == len(categoria)):
        print("Saliendo..")
    producto = Producto(nombre_producto, precio,categoria[cat -1])
    menu.append(producto)

    for elem in menu:
         print(elem._nombre,"\n",elem._precio,"\n",elem._categoria,"\n")
    return menu



def eliminarProducto(menu):
    i = 1
    print("Elija el producto que quiere eliminar:\n")
    for elem in menu:
        print(f"{i}-",elem._nombre)
        i += 1

    prodAElim = int(input(""))
    if(prodAElim > 0 and prodAElim <= len(menu)):
        del menu[prodAElim -1]
    else:
        print("Opcion seleccionada incorrecta\n")
    
    for elem in menu:
        print(elem._nombre,"\n",elem._precio,"\n",elem._categoria,"\n")
    return menu


def modificarProducto(menu):
    i = 1
    print("Elija el producto que quiere modificar:\n")
    for elem in menu:
        print(f"{i}-",elem._nombre)
        i += 1
    prodAModif = int(input(""))
    if(prodAModif > 0 and prodAModif <= len(menu)):
        print("Que queres modificar del producto:\n")
        print("1 - Nombre\n2 - Precio\n3- Categoria")
        op = int(input(""))

        if(op == 1):
            nuevo_Nomb = input("Ingrese el nuevo nombre del producto:\n")
            menu[op-1].set_nombre(nuevo_Nomb)
            print("Nombre cambiado con exito")
            return
        elif(op == 2):
            nuevo_Precio = int(input("Ingrese el nuevo precio del producto:\n"))
            menu[op-1].set_precio(nuevo_Precio)
            print("Precio cambiado con exito\n")
            return
        elif(op == 3):
                i = 1
                print("Elija la nueva categoria")
                for elem in categoria:
                    print(f"{i}-",elem)
                    i += 1
                nuevo_Cat = int(input(""))
                print(categoria[nuevo_Cat-1])
                if(nuevo_Cat == 1):
                        menu[prodAModif-1].set_categoria(categoria[nuevo_Cat-1])
                        print("Categoria cambiada\n")
                        for elem in menu:
                            print(elem._nombre,"\n",elem._precio,"\n",elem._categoria,"\n")
                        return
                elif(nuevo_Cat == 2):
                        menu[prodAModif-1].set_categoria(categoria[nuevo_Cat-1])
                        print("Categoria cambiada\n")
                        for elem in menu:
                            print(elem._nombre,"\n",elem._precio,"\n",elem._categoria,"\n")
                        return
                elif(nuevo_Cat == 3):
                    menu[prodAModif-1].set_categoria(categoria[nuevo_Cat-1])
                    print("Categoria cambiada\n")
                    for elem in menu:
                        print(elem._nombre,"\n",elem._precio,"\n",elem._categoria,"\n") 
                    return
                else:
                    print("Opciones incorrecte\n")
                    return
        else:
            print("Opcion incorrecta\n")
        menu[prodAModif - 1]
    else:
        print("Opcion seleccionada incorrecta\n")
        return
    return menu