from kivy.app import App
from pedidos.pedidos import PedidoApp
from kivy.core.window import Window

if __name__ == "__main__":
    # Establecer el tamaño mínimo de la ventana
    Window.minimum_width = 400
    Window.minimum_height = 700
    
    # Configurar la ventana para que no sea redimensionable
    Window.size = (400, 700)
    Window.resizable = False

    PedidoApp().run()