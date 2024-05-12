from kivy.uix.screenmanager import Screen
from kivy.app import App
from pedidos.pedidos import PedidoApp  # Asegúrate de importar correctamente la clase PedidoApp

class HomeScreen(Screen, App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def open_pedido_app(self):
        # Obtén la instancia de la aplicación actual
        app = App.get_running_app()
        # Obtén la instancia de PedidoApp
        pedido_app = PedidoApp()
        # Inicia la aplicación de PedidoApp
        pedido_app.run()
        # Cierra la aplicación actual
        app.stop()

    def agregar_modificar_producto(self):
        print("Agregando o modificando producto...")

    def reporte_ventas(self):
        print("Generando reporte de ventas...")

    def salir(self):
        print("Saliendo del programa.")
        App.get_running_app().stop()
