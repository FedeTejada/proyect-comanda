# frame_config.py
import tkinter as tk
from customtkinter import CTkFrame

def frame_config(frame):
    # Aquí iría el contenido de la sección
    label = tk.Label(frame, text="Bienvenido a la sección Configuracion", fg='white', bg='black')
    label.pack()
