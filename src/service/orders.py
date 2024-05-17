import tkinter as tk
from tkinter import messagebox, simpledialog
from customtkinter import CTkFrame, CTkButton, CTkInputDialog, CTkScrollableFrame

product_buttons = {}  # Dictionary to store product buttons and their quantities
selected_products = {}  # Dictionary to store selected products and their quantities

def add_to_cart(product):
    global selected_products
    if product in selected_products:
        quantity_dialog = CTkInputDialog(title="Quantity", text=f"Enter quantity for {product}:", initialvalue=selected_products[product])
        quantity = quantity_dialog.get_input()  # Use get_input attribute to retrieve the input value
    else:
        quantity_dialog = CTkInputDialog(title="Quantity", text=f"Enter quantity for {product}:")
        quantity = quantity_dialog.get_input()
    
    if quantity is not None:
        try:
            quantity = int(quantity)  # Convert quantity to integer
            selected_products[product] = quantity
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for quantity.")
    update_cart_display()

# Update remove_from_cart to delete all items from the cart
def remove_from_cart():
    global selected_products
    if messagebox.askokcancel("Remove All", "Do you want to remove all items from the cart?"):
        selected_products = {}
        update_cart_display()

def update_cart_display():
    global selected_products
    cart_listbox.delete(0, tk.END)
    for product, quantity in selected_products.items():
        cart_listbox.insert(tk.END, f"{product} x {quantity}")
    total_price = sum(quantity * 10 for quantity in selected_products.values())
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
    height_button = 80
    pad_y = 8
    side_text = 'center'
    if len(product_list) > 30:
        num_columns = 1  # Change to single column layout if more than 30 products
        height_button = 25
        pad_y = 2
    for i, product in enumerate(product_list):
        row_num = i // num_columns
        col_num = i % num_columns
        product_button = CTkButton(products_frame,
                                   text=product,
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
        product_buttons[product] = product_button  # Add button to the dictionary
        products_frame.grid_columnconfigure(col_num, weight=1)  # Columns should expand
        products_frame.grid_rowconfigure(row_num, weight=1)  # Rows should expand


def on_resize(event):
    global product_buttons  # Declare product_buttons as global
    # Adjust the size of product buttons based on the window width and maintain square aspect ratio
    new_width = max(80, (event.width - 16) // 5)  # Considering horizontal padding
    new_height = new_width  # Maintain square aspect ratio
    for button in product_buttons.values():
        button.config(width=new_width, height=new_height)

def frame_orders(frame):
    frame.grid_columnconfigure(0, weight=2)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_rowconfigure(0, weight=1)
    frame.configure(fg_color="#f2f2f2")

    products_frame = CTkScrollableFrame(frame, corner_radius=0, fg_color="#f2f2f2")
    products_frame.grid(row=0, column=0, sticky="nsew")

    product_list = ["Product 1", "Product 2", "Product 3"] * 13
    show_products(products_frame, product_list)

    global cart_listbox, total_label
    cart_frame = CTkFrame(frame, corner_radius=0, fg_color="#fff", width=200)
    cart_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    cart_listbox = tk.Listbox(cart_frame, font=("Helvetica", 12), borderwidth=0)
    cart_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    button_frame = CTkFrame(cart_frame, corner_radius=0, fg_color="#f2f2f2")
    button_frame.pack(side="bottom", fill="x")

    # Move the total_label before the buttons
    total_label = tk.Label(button_frame, text="Total: $0", font=("Helvetica", 12))
    total_label.pack(side="top", padx=2, pady=5)

    # Load and display the remove button
    remove_button = CTkButton(button_frame, text="Clear Cart", command=remove_from_cart, fg_color="#FF0000", hover_color="#FF3333", height=40, width=10)
    remove_button.pack(side="left", padx=(0, 5), pady=10)

    finish_button = CTkButton(button_frame, text="Complete Purchase", command=finalize_purchase, fg_color="#008000", hover_color="#007300", height=40, width=25)
    finish_button.pack(side="right", padx=(5, 0), pady=10)

    # Configure cart_frame to expand vertically
    cart_frame.grid_rowconfigure(0, weight=1)

    # Bind double click event to remove item from cart
    cart_listbox.bind("<Double-Button-1>", lambda event: remove_item(event))

def remove_item(event):
    global selected_products
    index = cart_listbox.curselection()
    if index:
        item = cart_listbox.get(index)
        product, _ = item.split(" x ")
        if messagebox.askokcancel("Remove Item", f"Do you want to remove {product} from the cart?"):
            del selected_products[product]
            update_cart_display()