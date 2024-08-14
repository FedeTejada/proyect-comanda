# ui/product_ui.py
from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkScrollableFrame, CTkToplevel
from tkinter import filedialog, Menu

def create_product_table_headers(frame):
    headers_frame = CTkFrame(frame, fg_color="#444", height=30)
    headers_frame.pack(fill='x', padx=10, pady=5)
    headers_frame.grid_columnconfigure(0, weight=1)
    headers_frame.grid_columnconfigure(1, weight=20)
    headers_frame.grid_columnconfigure(2, weight=1)

    CTkLabel(headers_frame, text="ID", fg_color='#444', text_color='white', font=('TkDefaultFont', 14, 'bold')).grid(row=0, column=0, padx=(20, 20), sticky='w')
    CTkLabel(headers_frame, text="PRODUCTO", fg_color='#444', text_color='white', font=('TkDefaultFont', 14, 'bold')).grid(row=0, column=1, padx=(0, 20))
    CTkLabel(headers_frame, text="PRECIO", fg_color='#444', text_color='white', font=('TkDefaultFont', 14, 'bold')).grid(row=0, column=2, padx=(0, 20), sticky='e')

def create_scrollable_product_frame(frame):
    scrollable_frame = CTkScrollableFrame(frame, fg_color="#555", width=780, height=100)
    scrollable_frame.pack(fill='both', expand=True, padx=10, pady=5)
    return scrollable_frame

def create_buttons_frame(frame, add_product_callback):
    buttons_frame = CTkFrame(frame, fg_color="#333")
    buttons_frame.pack(fill='x', padx=10, pady=10)
    add_button = CTkButton(buttons_frame, text="Agregar producto", font=('TkDefaultFont', 11, 'bold'), fg_color="#4CAF50", hover_color="#45A049", height=40, command=add_product_callback)
    add_button.pack(side='right', padx=10)
