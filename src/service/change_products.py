# change_product.py
from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel, CTkScrollableFrame

def frame_modif_product(frame):
    """
    Defines the main content frame for product modification.
    """
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
    CTkLabel(headers_frame, text="PRODUCT", fg_color='#444', text_color='white', font=('TkDefaultFont', 14, 'bold')).grid(row=0, column=1, padx=(0, 20))
    CTkLabel(headers_frame, text="CATEGORY", fg_color='#444', text_color='white', font=('TkDefaultFont', 14, 'bold')).grid(row=0, column=2, padx=(0, 20), sticky='e')

    # Create a scrollable frame to contain the product rows
    scrollable_frame = CTkScrollableFrame(frame, fg_color="#555", width=780, height=100)
    scrollable_frame.pack(fill='both', expand=True, padx=10, pady=5)

    # Add rows for products (example with 30 rows)
    # ESE 30 TIENE QUE SER EN REALIDAD LA CANTIDAD REAL DE PRODUCTOS QUE HAY CARGADOS
    for _ in range(30):
        row_frame = CTkFrame(scrollable_frame, fg_color="#666", height=25)
        row_frame.pack(fill='x', padx=5, pady=2)
        
        # Configure the grid columns to ensure separation
        row_frame.grid_columnconfigure(0, weight=1)
        row_frame.grid_columnconfigure(1, weight=20)
        row_frame.grid_columnconfigure(2, weight=1)
        
        # Create labels for product rows
        # ACA TIENE QUE IR CADA VARIABLE, UNA CORRESPONDIENTE PARA CADA CARACTERISTICA DEL PRODUCTO (ID, PRODUCT, CATEGORY)
        CTkLabel(row_frame, text="ID", fg_color='#666', text_color='white').grid(row=0, column=0, padx=(10, 20), sticky='w')
        CTkLabel(row_frame, text="PRODUCT", fg_color='#666', text_color='white').grid(row=0, column=1, padx=(0, 20))
        CTkLabel(row_frame, text="CATEGORY", fg_color='#666', text_color='white').grid(row=0, column=2, padx=(0, 10), sticky='e')

    # Create the buttons for adding and removing products
    buttons_frame = CTkFrame(frame, fg_color="#333")
    buttons_frame.pack(fill='x', padx=10, pady=10)
    
    # --------------------------------------------------------------------------
    # NO LAS CREE PERO DEBERIA DE HABER UNA FUNCION DE AGREGAR PRODUCTO Y DE BORRAR PRODUCTO, NO SE COMO HACERLAS PERO CUANDO ESTE SOLCIONADO LO DE ARRIBA Y YO DESPUES VEMOS JUNTOS ESTO
    # Create "Add Product" button
    add_button = CTkButton(buttons_frame, text="Add Product", font=('TkDefaultFont', 11, 'bold'), fg_color="#4CAF50", hover_color="#45A049", height=40)
    add_button.pack(side='left', padx=10)
    
    # Create "Remove Product" button
    remove_button = CTkButton(buttons_frame, text="Remove Product", font=('TkDefaultFont', 11, 'bold'), fg_color="#F44336", hover_color="#E53935", height=40)
    remove_button.pack(side='right', padx=10)
    # --------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# End of script
