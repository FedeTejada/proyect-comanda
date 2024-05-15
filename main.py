# Importan modulos
from src.models.Product import Product
from src.models.Order import Order
# Corre programa
def main():
    # Un while true para que se repita hasta que se diga lo contrario
    # while True:
    #     # Pantalla principal con menu de opciones
    #     print("\n¿Que desea realizar?")
    #     print("\n1. Tomar pedidos")
    #     print("2. Cambiar precios")
    #     print("3. Reportar balances")
    #     print("4. Salir")

    #     # El usuario elige la operacion que quiere realizar
    #     opcion = input("Seleccione una opción: ")

    #     if opcion == "1":
    #         return
        
    #     elif opcion == "2":
    #         return
        
    #     elif opcion == "3":
    #         return
        
    #     elif opcion == "4":
    #         print("Saliendo del programa.")
    #         break

    #     # En caso de elegir una operacion incorrecta salta una advertencia y se reinicia el while
    #     else:
    #         print("Opción no válida. Por favor, seleccione una opción válida.")

# Si el archivo es el main se lo llama


    lomito = Product(1,"lomito",500,"sandwich")
    print(lomito.getName())
    print(lomito.getPrice())
#Correr programa
if __name__ == "__main__":
        main()
