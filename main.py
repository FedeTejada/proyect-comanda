from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from clases.home_screen import HomeScreen
from pedidos.pedidos import PedidoApp

class HomeApp(App):
    def build(self):
        # Crea una instancia de ScreenManager
        sm = ScreenManager()

        # Crea una instancia de PedidoApp
        pedido_app = PedidoApp()

        # Agrega una instancia de HomeScreen al ScreenManager
        home_screen = HomeScreen(name='home')
        home_screen.ids.home_button.bind(on_release=home_screen.open_pedido_app)
        sm.add_widget(home_screen)

        return sm

if __name__ == '__main__':
    HomeApp().run()
