# orders.py
import tkinter as tk
from tkinter import messagebox
from customtkinter import CTkFrame, CTkButton, CTkInputDialog, CTkScrollableFrame
from controller.OrderController import OrderController

product_buttons = {}
order_controller = OrderController()

def add_to_cart(product):
    quantity_dialog = CTkInputDialog(title="Quantity", text=f"Enter quantity for {product.name}:")
    quantity = quantity_dialog.get_input()
    if quantity is not None:
        try:
            quantity = int(quantity)
            order_controller.add_to_cart(product, quantity)
            update_cart_display()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for quantity.")

def update_cart_display():
    cart_listbox.delete(0, tk.END)
    total_price = order_controller.get_total_price()
    for product_name, quantity in order_controller.selected_products.items():
        cart_listbox.insert(tk.END, f"{product_name} x {quantity}")
    total_label.config(text=f"Total: ${total_price}")

def remove_from_cart():
    if messagebox.askokcancel("Remove All", "Do you want to remove all items from the cart?"):
        order_controller.remove_from_cart()
        update_cart_display()

def remove_item(event):
    index = cart_listbox.curselection()
    if index:
        item = cart_listbox.get(index)
        product_name, _ = item.split(" x ")
        if messagebox.askokcancel("Remove Item", f"Do you want to remove {product_name} from the cart?"):
            order_controller.remove_item(product_name)
            update_cart_display()

def finalize_purchase():
    if not order_controller.selected_products:
        messagebox.showerror("Error", "No products in the cart.")
        return

    # Collect customer details
    name_dialog = CTkInputDialog(title="Customer Name", text="Enter the name of the customer:")
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
    
    cadet_dialog = CTkInputDialog(title="Obserevation", text="do u want to do an observation? (optional):")
    observation = cadet_dialog.get_input()
    
    if cadet_option == "yes":
        cadete = True
    else:
        cadete = False

    # Call finalize_purchase on the controller
    order_controller.finalize_purchase(customer_name, pickup_time, cadete, cadet_address, observation)
    messagebox.showinfo("Order Confirmed", "Your order has been confirmed.")
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

    cart_frame.grid_rowconfigure(0, weight=1)
    cart_listbox.bind("<Double-Button-1>", lambda event: remove_item(event))