# controllers/product_controller.py
from service.serviceProduct import getProducts, updateProduct, deleteProduct, addProducts

def refresh_products(scrollable_frame):
    for widget in scrollable_frame.winfo_children():
        widget.destroy()
    products = getProducts()
    for product in products:
        # Aquí colocarías el código para crear cada fila de producto
        pass

def save_changes(product, name, price, refresh_callback, window):
    updateProduct(product.id, name, price)
    refresh_callback()
    window.destroy()

def save_new_product(name, price, refresh_callback, window):
    addProducts(name, price)
    refresh_callback()
    window.destroy()
