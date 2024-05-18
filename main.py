# main.py
import tkinter as tk
import customtkinter
from customtkinter import *
from PIL import Image, ImageTk
from src.service.home import frame_home
from src.service.orders import frame_orders
from src.service.change_products import frame_modif_product
from src.service.balance import frame_balance
from src.service.config import frame_config

# ------------------------------------------------------------------------------
# FUNCTION TO CHANGE THE MAIN CONTENT

def change_section(frame, seccion_funcion):
    """
    Clear the current frame and load a new section.
    """
    for widget in frame.winfo_children():
        widget.destroy()
    seccion_funcion(frame)

# ------------------------------------------------------------------------------
# CONFIGURATION OF THE WINDOW

root = customtkinter.CTk()
root.title("Comandero")
customtkinter.set_appearance_mode("system")  # Set the appearance mode to system default

# Window dimensions
width = 1200
height = 600

# Calculating the x and y position for centering the window
pos_x = int(root.winfo_screenwidth() / 2 - width / 2)
pos_y = int(root.winfo_screenheight() / 2 - height / 2)

# Set the size and position of the window
root.geometry(f"{width}x{height}+{pos_x}+{pos_y}")

# Set minimum window size
root.minsize(1200, 600)  # Minimum width: 1200px, minimum height: 600px

# ------------------------------------------------------------------------------
# NAVIGATION BAR CONFIGURATION

frame_nav = CTkFrame(root, 
                     width=220,
                     corner_radius=0,
                     fg_color="#222",
                     border_color="#0F0F0F",
                     border_width=1)
frame_nav.pack(side="left", fill="y")
frame_nav.propagate(False)

frame_content = CTkFrame(root, corner_radius=0)
frame_content.pack(side="right", expand=True, fill="both")

# ------------------------------------------------------------------------------
# NAV BAR BUTTONS CONFIGURATION

# Home Button
home_button_img_pil = Image.open(".\media\images\home_icon.png")
home_button_img = CTkImage(home_button_img_pil)

home_button = CTkButton(
                frame_nav,
                text="",
                image=home_button_img,
                compound="left",
                command=lambda: change_section(frame_content, frame_home),
                width=160,
                height=40)
home_button.pack(pady=(40, 10), padx=10, anchor="center")

# List of buttons and their corresponding functions
buttons = [
    ("Tomar Pedidos", frame_orders),
    ("Modificar Productos", frame_modif_product),
    ("Ver Balance", frame_balance),
]

# Create and pack each button in the navigation bar
for text, function in buttons:
    btn = CTkButton(
        frame_nav,
        text=text,
        command=lambda f=frame_content, fn=function: change_section(f, fn),
        width=160,
        height=40)
    btn.pack(pady=10, padx=10, anchor="center")

# Configuration Button
config_button = CTkButton(
                    frame_nav,
                    text="Configuracion",
                    command=lambda: change_section(frame_content, frame_config),
                    fg_color="#808080",
                    hover_color="#676767")
config_button.pack(side="bottom", pady=(10, 40), padx=10, anchor="center")

# ------------------------------------------------------------------------------
# START THE MAIN LOOP

root.mainloop()
