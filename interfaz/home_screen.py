from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from pedidos.pedidos import PedidoApp  # Importar la clase PedidoApp

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

        # Botón para ejecutar PedidoApp
        btn = Button(text='Abrir PedidoApp')
        btn.bind(on_press=self.get_ejecutar_pedido_app())  # Asociar la función al evento on_press del botón
        self.add_widget(btn)

    def get_ejecutar_pedido_app(self):
        def ejecutar_pedido_app(instance):
            # Ejecutar la clase PedidoApp
            PedidoApp().run()
        return ejecutar_pedido_app
