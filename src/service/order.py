import tkinter as tk
from tkinter import messagebox, simpledialog
from customtkinter import CTkButton, CTkInputDialog

product_buttons = {}  # Dictionary to store product buttons and their quantities
selected_products = {}  # Dictionary to store selected products and their quantities

def add_to_cart(product):
    global selected_products
    if product in selected_products:
        quantity_dialog = CTkInputDialog(title="Quantity", text=f"Enter quantity for {product}:", initialvalue=selected_products[product])
        quantity = quantity_dialog.get_input()  # Use get_input attribute to retrieve the input value
    else:
        quantity_dialog = CTkInputDialog(title="Quantity", text=f"Enter quantity for {product}:")
        quantity = quantity_dialog.get_input()  # Use get_input attribute to retrieve the input value
    
    if quantity is not None:
        try:
            quantity = int(quantity)  # Convert quantity to integer
            selected_products[product] = quantity
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for quantity.")
    update_cart_display()

def remove_from_cart():
    global cart_listbox, selected_products
    # Get the selected index in the list
    selected_index = cart_listbox.curselection()
    if selected_index:
        # Get the selected product
        selected_product = cart_listbox.get(selected_index)
        # Split the product name and quantity
        product, _ = selected_product.split(" x ")
        # Remove the selected product from the selected products dictionary
        del selected_products[product]
        # Update the cart display
        update_cart_display()

def update_cart_display(cart_listbox, total_label):
    global selected_products
    cart_listbox.delete(0, tk.END)  # Clear the listbox
    # Display selected products in the listbox
    for product, quantity in selected_products.items():
        cart_listbox.insert(tk.END, f"{product} x {quantity}")
    # Calculate and display the total price
    total_price = sum(quantity * 10 for quantity in selected_products.values())  # Assuming each product costs $10
    total_label.config(text=f"Total: ${total_price}")

def finalize_purchase():
    # Show a dialog box to confirm the purchase
    confirm = messagebox.askquestion("Confirm", "Do you want to finalize the purchase?")
    if confirm == "yes":
        # Logic to finalize the purchase
        pass

def show_products(products_frame, product_list):
    global product_buttons  # Declare product_buttons as global
    num_columns = 5  # Number of columns before jumping to the next row
    for i, product in enumerate(product_list):
        row_num = i // num_columns
        col_num = i % num_columns
        product_button = CTkButton(products_frame,
                                   text=product,
                                   command=lambda p=product: add_to_cart(p),
                                   width=80,
                                   height=80,
                                   font=("Helvetica", 16),
                                   text_color="#333",
                                   hover_color="#b3b3b3",
                                   border_color="#c4c4c4",
                                   border_width=2,
                                   fg_color="#d9d9d9")
        product_button.grid(row=row_num, column=col_num, padx=8, pady=8, sticky="nsew")
        product_buttons[product] = product_button  # Add button to the dictionary
        products_frame.grid_columnconfigure(col_num, weight=1)  # Columns should expand
        products_frame.grid_rowconfigure(row_num, weight=1)  # Rows should expand
