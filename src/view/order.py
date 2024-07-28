# orders.py
import tkinter as tk
import time
from tkinter import messagebox
from customtkinter import CTkFrame, CTkButton, CTkInputDialog, CTkScrollableFrame
from src.controller.OrderController import OrderController
from src.service.serviceProduct import getProducts
from win32printing import Printer
product_buttons = {}
order_controller = OrderController()

def add_to_cart(product):
    quantity_dialog = CTkInputDialog(title="Cantidad", text=f"Ingrese la cantidad de {product.name}:")
    quantity = quantity_dialog.get_input()
    if quantity is not None:
        try:
            quantity = int(quantity)
            order_controller.add_to_cart(product, quantity)
            update_cart_display()
        except ValueError:
            messagebox.showerror("Error", "Ingrese una cantiad valida")
def update_cart_display():
    cart_listbox.delete(0, tk.END)
    total_price = order_controller.get_total_price()
    for product_name, quantity in order_controller.selected_products.items():
        cart_listbox.insert(tk.END, f"{product_name} x {quantity}")
    total_label.config(text=f"Total: ${total_price}")

def remove_from_cart():
    if messagebox.askokcancel("Eliminar todo", "Desea eliminar todos los items del carrito?"):
        order_controller.remove_from_cart()
        update_cart_display()

def remove_item(event):
    index = cart_listbox.curselection()
    if index:
        item = cart_listbox.get(index)
        product_name, _ = item.split(" x ")
        if messagebox.askokcancel("Eliminar item", f"Quieres eliminar {product_name} del carrito?"):
            order_controller.remove_item(product_name)
            update_cart_display()

def finalize_purchase():
    """
    Finalize the purchase and show a confirmation dialog.
    """
    # Define font configurations
    title_font = {
        "height": 20,
        "weight": 800,
    }

    normal_font = {
        "height": 14,
    }

    # Collect customer details
    name_dialog = CTkInputDialog(title="Nombre del cliente", text="Ingrese el nombre:")
    customer_name = name_dialog.get_input()
    if customer_name is None:
        return

    time_dialog = CTkInputDialog(title="Hora", text="Para que hora seria:")
    pickup_time = time_dialog.get_input()
    if pickup_time is None:
        return

    cadet_dialog = CTkInputDialog(title="Delivery", text="Quiere cadete? (Si/No):")
    cadet_option = cadet_dialog.get_input()
    if cadet_option is None:
        return

    cadet_address = None
    if cadet_option.lower() == "si" or cadet_option.lower() == "s":
        cadet_option = 1
        address_dialog = CTkInputDialog(title="Direccion", text="Ingrese la direcion a enviar:")
        cadet_address = address_dialog.get_input()
        if cadet_address is None:
            return
    else:
        cadet_option = 0
    observation_dialog = CTkInputDialog(title="Observaciones", text="Alguna observacion? (opcional):")
    observation = observation_dialog.get_input()

    # Get the total price from the label
    total_price = total_label.cget("text").split(": $")[1]

    # Print the order details
    with Printer(linegap=5) as printer:
        
        printer.text(f"--- {customer_name} ---", font_config=title_font)
        printer.text(" ")

        for product_name, quantity in order_controller.selected_products.items():
            # Find the product in the menu to get its price
            product = next((p for p in getProducts() if p.name == product_name), None)
            if product:
                printer.text(f"{product.name} - ${product.price} x {quantity}u", font_config=normal_font)
                printer.text(" ")
        
        printer.text(" ")
        printer.text(f"HORA: {pickup_time}", font_config=normal_font)
        printer.text(" ")
        if cadet_address:
            printer.text(f"DIRECCIÓN: {cadet_address}", font_config=normal_font)
            printer.text(" ")
        if observation:
            printer.text(f"OBS: {observation}", font_config=normal_font)
            printer.text(" ")
        printer.text(f"${total_price}", font_config=title_font)

    # Show confirmation message
    messagebox.showinfo("Orden confirmada", "La compra fue confirmada")
    order_controller.finalize_purchase(customer_name, pickup_time, cadet_option, cadet_address, observation)
    # Update cart display (assumed to clear the current cart)
    update_cart_display()

def show_products(products_frame):
    menu = order_controller.get_menu()
    num_columns = 5  # Number of columns before jumping to the next row
    height_button = 80
    pad_y = 8

    if len(menu) > 30:
        num_columns = 1
        height_button = 25
        pad_y = 2

    for i, product in enumerate(menu):
        row_num = i // num_columns
        col_num = i % num_columns
        product_button = CTkButton(products_frame,
                                   text=product.name,
                                   command=lambda p=product:add_to_cart(p),
                                   width=80,
                                   height=height_button,
                                   font=("Helvetica", 16),
                                   text_color="#333",
                                   hover_color="#b3b3b3",
                                   border_color="#c4c4c4",
                                   border_width=2,
                                   fg_color="#d9d9d9")
        product_button.grid(row=row_num, column=col_num, padx=8, pady=pad_y, sticky="nsew")
        product_buttons[product.name] = product_button
        products_frame.grid_columnconfigure(col_num, weight=1)
        products_frame.grid_rowconfigure(row_num, weight=1)

def frame_orders(frame):
    frame.grid_columnconfigure(0, weight=2)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_rowconfigure(0, weight=1)
    frame.configure(fg_color="#f2f2f2")

    products_frame = CTkScrollableFrame(frame,
                                        corner_radius=0,
                                        fg_color="#f2f2f2")
    products_frame.grid(row=0, column=0, sticky="nsew")

    show_products(products_frame)

    global cart_listbox, total_label
    cart_frame = CTkFrame(frame,
                          corner_radius=0,
                          fg_color="#fff",
                          width=200)
    cart_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    cart_listbox = tk.Listbox(cart_frame,
                              font=("Helvetica", 12),
                              borderwidth=0)
    cart_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    button_frame = CTkFrame(cart_frame,
                            corner_radius=0,
                            fg_color="#f2f2f2")
    button_frame.pack(side="bottom", fill="x")

    total_label = tk.Label(button_frame,
                           text="Total: $0",
                           font=("Helvetica", 12))
    total_label.pack(side="top", padx=2, pady=5)

    remove_button = CTkButton(button_frame,
                              text="Limpiar carrito",
                              command=remove_from_cart,
                              fg_color="#FF0000",
                              hover_color="#FF3333",
                              height=40,
                              width=10)
    remove_button.pack(side="left", padx=(0, 5), pady=10)

    finish_button = CTkButton(button_frame,
                              text="Finalizar compra",
                              command=finalize_purchase,
                              fg_color="#008000",
                              hover_color="#007300",
                              height=40,
                              width=25)
    finish_button.pack(side="right", padx=(5, 0), pady=10)

    cart_frame.grid_rowconfigure(0, weight=1)
    cart_listbox.bind("<Double-Button-1>", lambda event: remove_item(event))