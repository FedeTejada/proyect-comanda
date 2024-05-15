import tkinter as tk
import customtkinter
from tkinter import messagebox, ttk
from customtkinter import CTkFrame, CTkButton

def add_to_cart(product):
    # Logic to add the product to the cart
    pass

def finalize_purchase():
    # Show a dialog box to confirm the purchase
    confirm = messagebox.askquestion("Confirm", "Do you want to finalize the purchase?")
    if confirm == "yes":
        # Logic to finalize the purchase
        pass

def show_products(products_frame, product_list):
    num_columns = 5  # Number of columns before jumping to the next row
    for i, product in enumerate(product_list):
        row_num = i // num_columns
        col_num = i % num_columns
        product_button = CTkButton(products_frame,
                                text=product,
                                command=lambda p=product: add_to_cart(p),
                                width=80,
                                height=80,
                                )
        product_button.grid(row=row_num, column=col_num, padx=8, pady=8)


def frame_orders(frame):
    frame.grid_columnconfigure(0, weight=2)  # Make the first column (products list) wider
    frame.grid_columnconfigure(1, weight=1)  # Make the second column (cart) narrower
    frame.grid_rowconfigure(0, weight=1)     # Make the first row (products and cart) expandable

    products_frame = customtkinter.CTkScrollableFrame(frame, corner_radius=0)
    products_frame.grid(row=0, column=0, sticky="nsew")

    # Example list of products
    product_list = ["Product 1", "Product 2", "Product 3"] * 10  # Repeat to fill space
    show_products(products_frame, product_list)

    cart_frame = CTkFrame(frame, corner_radius=0, bg_color="#fff")
    cart_frame.grid(row=0, column=1, sticky="nsew")
    
    # show_cart(cart_frame)

    # Set the minimum width for the cart frame
    cart_frame.update_idletasks()
    cart_frame_width = max(300, cart_frame.winfo_reqwidth())  # Ensure a minimum width of 300 pixels
    cart_frame.config(width=cart_frame_width)

    button_frame = CTkFrame(cart_frame)
    button_frame.pack(side="bottom", fill="x")

    finish_button = CTkButton(cart_frame, text="Complete Purchase", command=finalize_purchase)
    finish_button.pack(side="bottom", padx=10, pady=10)

    # Configure rows in products_frame to expand vertically
    for i in range(10):  # Assuming there are 10 rows
        products_frame.grid_rowconfigure(i, weight=1)

    # Allow cart frame to expand horizontally
    cart_frame.grid_columnconfigure(0, weight=10)
