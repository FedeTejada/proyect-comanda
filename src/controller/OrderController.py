from src.service.service_order import *
from src.service.service_pro_ord import *
from src.service.serviceProduct import *
import logging


logging.basicConfig( 
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%d-%m-%y %H:%M:%S"
)
logger = logging.getLogger(__name__)

class OrderController:
    def __init__(self): # instancio la clase, con los atributos necesarios para llevar a cabo una orden
        self.menu = getProducts()
        self.order = create_order(False, "Desconocida", "Desconocida") # creo una orden "vacia" para poder crear los objetos ordenXproduc
        self.selected_products = {} # diccionario con productos y cantidad
        self.list_product = [] # lista de producto_orden

    # añade al pedido un producto, como un objeto producto_orden
    def add_to_cart(self, product, quantity):
        order_id = self.order.get_id()
        product_id = product.id
        product_order = add_product_order(product_id, order_id, quantity) # funcion del services para crear el producto orden
        self.selected_products[product.name] = quantity # diccionario con nombre y cantidad
        self.list_product.append(product_order)
        
    # elimina todos los productos dentro de la lista y tambien del diccionario
    def remove_from_cart(self):
        self.selected_products = {}
        self.list_product.clear()
        logger.info("Todos los items del carrito han sido eliminados")

    # elimina solo un producto de la lista y del diccionario
    def remove_item(self, product_name):
        product_order_to_remove = None
        for product_order in self.list_product:
            if product_order.product_id == get_product_id_by_name(product_name):
                product_order_to_remove = product_order
                break
        
        if product_order_to_remove:
            self.list_product.remove(product_order_to_remove)
            del self.selected_products[product_name]
    
    # funcion para guardar y finalizar el pedido
    def finalize_purchase(self, customer_name, pickup_time, cadet_option, cadet_address, observation):
        order_mod = mod_order(self.order, cadet_address, customer_name, pickup_time, observation, cadet_option)
        save_order(order_mod)
        for pro_ord in self.list_product:
            save_pro_ord(pro_ord)
        
        self.remove_from_cart()
        self.order =  create_order(False, "Desconocida", "Desconocida")
        logger.info(f"Orden finalizada y guardad en el db nro {order_mod.get_id()}")

    # metodo para obtener el precio total de la orden
    def get_total_price(self):
        total_price = 0
        for product in self.menu: # recorro el menu, controlo si esta en el diccionario de productos seleccionados
            if product.name in self.selected_products:
                total_price += product.price * self.selected_products[product.name] # si el producto esta, se multiplica con la cantidad correspondiente
        return total_price

    def get_menu(self):
        self.menu = getProducts()
        return self.menu
