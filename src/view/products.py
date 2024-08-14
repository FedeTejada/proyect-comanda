# change_product.py
from customtkinter import CTk
from ui.products_ui import create_product_table_headers, create_scrollable_product_frame, create_buttons_frame
from controller.product_controller import refresh_products, save_changes, save_new_product

def frame_modif_product(frame):
    frame.configure(fg_color='#333')
    create_product_table_headers(frame)
    scrollable_frame = create_scrollable_product_frame(frame)

    def add_product():
        def save_product_callback():
            # Llamar a save_new_product aquí
            save_new_product(name_entry.get(), price_entry.get(), lambda: refresh_products(scrollable_frame), top)

        top = CTkToplevel()
        top.title("Agregar producto")
        top.minsize(500, 500)
        # El código para crear la UI para agregar producto

    create_buttons_frame(frame, add_product)
    refresh_products(scrollable_frame)
