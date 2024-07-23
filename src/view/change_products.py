# change_product.py
from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel, CTkEntry, CTkScrollableFrame, CTkToplevel
from tkinter import filedialog, Menu
from service.serviceProduct import getProducts,updateProduct,deleteProduct, addProducts
import os

# ------------------------------------------------------------------------------
# PROVISIONAL VARIABLES
# List of products (example data)

# ------------------------------------------------------------------------------
# CHANGE PRODUCTS FRAME
def frame_modif_product(frame):
    """
    Defines the main content frame for product modification.
    """
    
    def refresh_products():
        """
        Refresh the product list displayed in the scrollable frame.
        """
        for widget in scrollable_frame.winfo_children():
            widget.destroy()
        
        products = getProducts()
        for product in products:
            row_frame = CTkFrame(scrollable_frame, fg_color="#666", height=25)
            row_frame.pack(fill='x', padx=5, pady=2)
            
            # Configure the grid columns to ensure separation
            row_frame.grid_columnconfigure(0, weight=1)
            row_frame.grid_columnconfigure(1, weight=20)
            row_frame.grid_columnconfigure(2, weight=1)
            
            # Create labels for product rows
            CTkLabel(row_frame, text=str(f"{product.id}"), fg_color='#666', text_color='white').grid(row=0, column=0, padx=(10, 20), sticky='w')
            CTkLabel(row_frame, text=str(f"{product.name}"), fg_color='#666', text_color='white').grid(row=0, column=1, padx=(0, 20))
            CTkLabel(row_frame, text=f"{product.price}", fg_color='#666', text_color='white').grid(row=0, column=2, padx=(0, 10), sticky='e')

            # Bind right-click event to the row frame
            row_frame.bind("<Button-3>", lambda e, p=product: show_context_menu(e, p))

    def show_context_menu(event, product):
        """
        Displays a context menu with options to modify or delete the product.
        """
        context_menu = Menu(frame, tearoff=0)
        context_menu.add_command(label="Modificar el produccto ", command=lambda: modify_product(product))
        context_menu.add_command(label="Eliminar el producto", command=lambda: delete_product(product))
        context_menu.post(event.x_root, event.y_root)

    def modify_product(product):
        """
        Opens a window to modify the selected product.
        """
        def save_changes():
            """
            Saves changes to the selected product and refreshes the display.
            """

            product_name = name_entry.get()
            product_price = price_entry.get()
            updateProduct(product.id,product_name,product_price)
            # product["image"] = image_path.get()
            refresh_products()
            top.destroy()

        def browse_image():
            """
            Opens a file dialog to select an image for the product.
            """
            image_file = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
            if image_file:
                image_path.set(image_file)

        top = CTkToplevel()
        top.title("Modificar Producto")
        top.minsize(500, 500)


        # Product Name entry
        CTkLabel(top, text="Nombre del producto:").pack(padx=20, pady=5)
        name_entry = CTkEntry(top)
        name_entry.pack(padx=10, pady=5)

        # Product Price entry
        CTkLabel(top, text="Precio del producto:").pack(padx=20, pady=5)
        price_entry = CTkEntry(top)
        price_entry.pack(padx=10, pady=5)

        # Product Image entry (optional)
        CTkLabel(top, text="Imagen del producto (Optional):").pack(padx=20, pady=5)
        image_path = CTkEntry(top, state='readonly')
        image_path.pack(padx=10, pady=5)

        browse_button = CTkButton(top, text="Explorar", command=browse_image)
        browse_button.pack(padx=20, pady=5)

        save_button = CTkButton(top, text="Guardar", command=save_changes)
        save_button.pack(padx=20, pady=20)

    def delete_product(product):
        """
        Deletes the selected product from the product list and refreshes the display.
        """
        deleteProduct(product.id)
        refresh_products()

    def add_product():
        """
        Opens a window to add a new product.
        """
        def save_product():
            """
            Saves the new product to the product list and refreshes the display.
            """
            product_name = name_entry.get()
            product_price = price_entry.get()
            # product_image = image_path.get()

            if not product_name or not product_price:
                return

            addProducts(product_name,product_price)


            refresh_products()
            top.destroy()

        def browse_image():
            """
            Opens a file dialog to select an image for the product.
            """
            image_file = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
            if image_file:
                image_path.set(image_file)

        # Create the top-level window for adding a product
        top = CTkToplevel()
        top.title("Agregar producto")
        top.minsize(500, 500)
        
        # Product Name entry
        CTkLabel(top, text="Nombre producto:").pack(padx=20, pady=5)
        name_entry = CTkEntry(top)
        name_entry.pack(padx=10, pady=5)

        # Product Price entry
        CTkLabel(top, text="Precio producto:").pack(padx=20, pady=5)
        price_entry = CTkEntry(top)
        price_entry.pack(padx=10, pady=5)

        # Product Image entry (optional)
        CTkLabel(top, text="Producto Imagen (Optional):").pack(padx=20, pady=5)
        image_path = CTkEntry(top, state='readonly')
        image_path.pack(padx=10, pady=5)

        # Browse button to select an image
        browse_button = CTkButton(top, text="Explorar", command=browse_image)
        browse_button.pack(padx=20, pady=5)

        # Save button to add the product
        save_button = CTkButton(top, text="Guardar", command=save_product)
        save_button.pack(padx=20, pady=20)

    # Configure the main frame
    frame.configure(fg_color='#333')  # Background color of the frame
    
    # Create the table header
    headers_frame = CTkFrame(frame, fg_color="#444", height=30)
    headers_frame.pack(fill='x', padx=10, pady=5)
    
    # Configure the grid columns to ensure separation
    headers_frame.grid_columnconfigure(0, weight=1)
    headers_frame.grid_columnconfigure(1, weight=20)
    headers_frame.grid_columnconfigure(2, weight=1)
    
    # Create labels for the table header
    CTkLabel(headers_frame, text="ID", fg_color='#444', text_color='white', font=('TkDefaultFont', 14, 'bold')).grid(row=0, column=0, padx=(20, 20), sticky='w')
    CTkLabel(headers_frame, text="PRODUCTO", fg_color='#444', text_color='white', font=('TkDefaultFont', 14, 'bold')).grid(row=0, column=1, padx=(0, 20))
    CTkLabel(headers_frame, text="PRECIO", fg_color='#444', text_color='white', font=('TkDefaultFont', 14, 'bold')).grid(row=0, column=2, padx=(0, 20), sticky='e')

    # Create a scrollable frame to contain the product rows
    scrollable_frame = CTkScrollableFrame(frame, fg_color="#555", width=780, height=100)
    scrollable_frame.pack(fill='both', expand=True, padx=10, pady=5)

    # Initially populate the product list
    refresh_products()

    # Create the buttons for adding and removing products
    buttons_frame = CTkFrame(frame, fg_color="#333")
    buttons_frame.pack(fill='x', padx=10, pady=10)

    # Create "Add Product" button
    add_button = CTkButton(buttons_frame, text="Agregar producto", font=('TkDefaultFont', 11, 'bold'), fg_color="#4CAF50", hover_color="#45A049", height=40, command=add_product)
    add_button.pack(side='right', padx=10)
    
    # Create "Remove Product" button
    # remove_button = CTkButton(buttons_frame, text="Remove Product", font=('TkDefaultFont', 11, 'bold'), fg_color="#F44336", hover_color="#E53935", height=40, command=remove_product)
    # remove_button.pack(side='right', padx=10)

# ------------------------------------------------------------------------------
#  END OF THE SCRIPT