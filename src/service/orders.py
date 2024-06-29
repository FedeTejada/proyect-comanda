# orders.py
from win32printing import Printer
import tkinter as tk
from tkinter import messagebox
from customtkinter import CTkFrame, CTkButton, CTkInputDialog, CTkScrollableFrame
from src.models.Product import Product

# ------------------------------------------------------------------------------
# ARRAY FOR TESTING
# Initialize some sample products and add them to a test menu array

lomito = Product(33, "Lomito", 100, "Sanguche")
pizza = Product(11, "Pizza", 500, "Pizza")
vianda_1 = Product(21, "Vianda 1", 400, "Vianda")
vianda_2 = Product(22, "Vianda 2", 400, "Vianda")
hamburguesa = Product(44, "Hamburguesa", 300, "Sanguche")
empanada = Product(55, "Empanada", 200, "Empanada")

menu = [lomito, pizza, vianda_1, vianda_2, hamburguesa, empanada]

# ------------------------------------------------------------------------------
# Variables
# Define dictionaries to store product buttons and selected products

product_buttons = {}  # Dictionary to store product buttons
selected_products = {}  # Dictionary to store selected products and their quantities

# ------------------------------------------------------------------------------
# Styles
title = {
    "height": 16,
    "weight": 800,
}

normal = {
    "height": 12,
}

# ------------------------------------------------------------------------------
# Functions

def add_to_cart(product):
    """
    Add a product to the cart or update its quantity.
    """
    global selected_products

    # Prompt for quantity
    quantity_dialog = CTkInputDialog(title="Quantity",
                                     text=f"Enter quantity for {product._name}:")
    quantity = quantity_dialog.get_input()

    if quantity is not None:
        try:
            quantity = int(quantity)  # Convert quantity to integer
            selected_products[product._name] = quantity
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for quantity.")

    update_cart_display()

def update_cart_display():
    """
    Update the cart display with selected products and calculate the total price.
    """
    global selected_products
    
    cart_listbox.delete(0, tk.END)
    total_price = 0
    for product_name, quantity in selected_products.items():
        cart_listbox.insert(tk.END, f"{product_name} x {quantity}")
        # Find the product in the menu to get its price
        product = next((p for p in menu if p._name == product_name), None)
        if product:
            total_price += product._price * quantity
    total_label.config(text=f"Total: ${total_price}")

def remove_from_cart():
    """
    Remove all items from the cart.
    """
    global selected_products
    if messagebox.askokcancel("Remove All", "Do you want to remove all items from the cart?"):
        selected_products = {}
        update_cart_display()

def remove_item(event):
    """
    Remove a single item from the cart.
    """
    global selected_products
    index = cart_listbox.curselection()
    if index:
        item = cart_listbox.get(index)
        product_name, _ = item.split(" x ")
        if messagebox.askokcancel("Remove Item", f"Do you want to remove {product_name} from the cart?"):
            del selected_products[product_name]
            update_cart_display()

def finalize_purchase():
    """
    Finalize the purchase and show a confirmation dialog.
    """
    global selected_products
    
    if not selected_products:
        messagebox.showerror("Error", "No products in the cart.")
        return

    # Collect customer details
    name_dialog = CTkInputDialog(title="Customer Name", text="Enter your name:")
    customer_name = name_dialog.get_input()

    if customer_name is None:
        return

    time_dialog = CTkInputDialog(title="Pickup Time", text="Enter the time you want the food:")
    pickup_time = time_dialog.get_input()

    if pickup_time is None:
        return

    cadet_dialog = CTkInputDialog(title="Delivery Option", text="Do you want a cadet? (yes/no):")
    cadet_option = cadet_dialog.get_input()

    if cadet_option is None:
        return

    cadet_address = None
    if cadet_option.lower() == "yes":
        address_dialog = CTkInputDialog(title="Address", text="Enter your address:")
        cadet_address = address_dialog.get_input()

        if cadet_address is None:
            return

    observation_dialog = CTkInputDialog(title="Observations", text="Any observations? (optional):")
    observation = observation_dialog.get_input()

    # Get the total price from the label
    total_price = total_label.cget("text").split(": $")[1]
    
    # Print the order details
    with Printer(linegap=5) as printer:
        printer.text(f"--- {customer_name} ---", font_config=title)
        printer.text(" ")
        printer.text(" ")
        for product_name, quantity in selected_products.items():
            # Find the product in the menu to get its price
            product = next((p for p in menu if p._name == product_name), None)
            printer.text(f"                    {product_name} x {quantity} - ${product._price}", font_config=normal)
        printer.text(" ")
        printer.text(" ")
        printer.text(f"HORA: {pickup_time}", font_config=normal)
        printer.text(" ")
        printer.text(f"CADETE: {cadet_option}", font_config=normal)
        if cadet_address:
            printer.text(f"DIRECCIÓN: {cadet_address}")
        printer.text(" ")
        printer.text(f"OBS: {observation}", font_config=normal)
        printer.text(" ")
        printer.text(" ")
        printer.text(f"                    ${total_price}", font_config=title)
    

    messagebox.showinfo("Order Confirmed", "Your order has been confirmed.")
    
    # BORRAR ESTO CUANDO SE HAGA, TIENEN QUE MANDAR EL selected_products A ALGUN LADO ANTES DE QUE YO LO RESETEE EN LA LINEA DE ACA ABAJO
    selected_products = {}
    update_cart_display()

def show_products(products_frame, menu):
    """
    Display the product buttons in the products frame.
    """
    global product_buttons
    num_columns = 5  # Number of columns before jumping to the next row
    height_button = 80
    pad_y = 8
    
    if len(menu) > 30:
        # Change to single column layout if more than 30 products
        num_columns = 1
        height_button = 25
        pad_y = 2
    
    for i, product in enumerate(menu):
        row_num = i // num_columns
        col_num = i % num_columns
        product_button = CTkButton(products_frame,
                                   text=product._name,
                                   command=lambda p=product: add_to_cart(p),
                                   width=80,
                                   height=height_button,
                                   font=("Helvetica", 16),
                                   text_color="#333",
                                   hover_color="#b3b3b3",
                                   border_color="#c4c4c4",
                                   border_width=2,
                                   fg_color="#d9d9d9")
        product_button.grid(row=row_num, column=col_num, padx=8, pady=pad_y, sticky="nsew")
        product_buttons[product._name] = product_button  # Use product._name as the key
        products_frame.grid_columnconfigure(col_num, weight=1)  # Columns should expand
        products_frame.grid_rowconfigure(row_num, weight=1)  # Rows should expand

def on_resize(event):
    """
    Adjust the size of product buttons based on the window width and maintain square aspect ratio.
    """
    global product_buttons
    new_width = max(80, (event.width - 16) // 5)  # Considering horizontal padding
    new_height = new_width  # Maintain square aspect ratio
    for button in product_buttons.values():
        button.config(width=new_width, height=new_height)

def frame_orders(frame):
    """
    Set up the orders frame layout and initialize the products and cart sections.
    """
    frame.grid_columnconfigure(0, weight=2)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_rowconfigure(0, weight=1)
    frame.configure(fg_color="#f2f2f2")

    products_frame = CTkScrollableFrame(frame,
                                        corner_radius=0,
                                        fg_color="#f2f2f2")
    products_frame.grid(row=0, column=0, sticky="nsew")

    show_products(products_frame, menu)

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

    # Move the total_label before the buttons
    total_label = tk.Label(button_frame,
                           text="Total: $0",
                           font=("Helvetica", 12))
    total_label.pack(side="top", padx=2, pady=5)

    # Load and display the remove button
    remove_button = CTkButton(button_frame,
                              text="Clear Cart",
                              command=remove_from_cart,
                              fg_color="#FF0000",
                              hover_color="#FF3333",
                              height=40,
                              width=10)
    remove_button.pack(side="left", padx=(0, 5), pady=10)

    finish_button = CTkButton(button_frame,
                              text="Complete Purchase",
                              command=finalize_purchase,
                              fg_color="#008000",
                              hover_color="#007300",
                              height=40,
                              width=25)
    finish_button.pack(side="right", padx=(5, 0), pady=10)

    # Configure cart_frame to expand vertically
    cart_frame.grid_rowconfigure(0, weight=1)

    # Bind double click event to remove item from cart
    cart_listbox.bind("<Double-Button-1>", lambda event: remove_item(event))

# ------------------------------------------------------------------------------
# End of script
