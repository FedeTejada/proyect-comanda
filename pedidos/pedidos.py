from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from clases.producto import Producto

class PedidoApp(App):
    def build(self):
        from clases.home_screen import HomeScreen
        # Inicializa variables
        self.menu = [
            Producto("Lomito", 100),
            Producto("Pizza", 200),
            Producto("Hamburguesa", 300),
            Producto("Empanada", 400),
            Producto("Cerveza", 50)
        ]
        self.carrito = []
        self.total = 0
        self.home_screen = HomeScreen(pedido_app=self)
        return self.home_screen

        # Crea el layout principal con un BoxLayout vertical
        self.layout_principal = BoxLayout(orientation='vertical')

        # Agrega la columna de productos a la primera posición
        self.layout_principal.add_widget(self.create_product_column())

        # Crea una columna para mostrar los elementos del carrito
        self.layout_carrito = ScrollView()  # Usamos ScrollView para el carrito
        self.layout_carrito.size_hint_y = None  # Desactivamos el tamaño automático
        self.layout_carrito.height = 300  # Establecemos una altura inicial

        self.layout_carrito_content = BoxLayout(orientation='vertical')
        self.layout_carrito.add_widget(self.layout_carrito_content)

        # Agrega el layout del carrito dentro del ScrollView
        self.layout_principal.add_widget(self.layout_carrito)

        # Agrega el botón de total
        self.total_button = Button(text=f"Total: ${self.total}", size_hint=(1, None), height=70,
                                   background_color=(0, 0.5, 1, 1), font_size=20, font_name='Arial', bold=True)
        self.total_button.bind(on_press=self.show_total_popup)
        self.layout_principal.add_widget(self.total_button)

        return self.layout_principal

    def create_product_column(self):
        layout_productos = BoxLayout(orientation='vertical')

        for producto in self.menu:
            btn = Button(text=producto._nombre, size_hint=(1, None), height=70)
            btn.producto = producto
            btn.bind(on_press=self.open_quantity_popup)
            layout_productos.add_widget(btn)

        return layout_productos

    def open_quantity_popup(self, instance):
        # Crea un nuevo BoxLayout para contener el TextInput y el botón de confirmación
        input_box = BoxLayout(orientation='horizontal')

        # Crea el TextInput
        content = TextInput(multiline=False)

        # Crea el botón de confirmación
        confirm_button = Button(text="Confirmar")
        confirm_button.bind(on_press=lambda _: self.on_confirm_button_press(content.text, instance.producto, popup))

        # Agrega el TextInput y el botón de confirmación al nuevo BoxLayout
        input_box.add_widget(content)
        input_box.add_widget(confirm_button)

        # Abre una ventana emergente para ingresar la cantidad
        popup = Popup(title='Cantidad', content=input_box, size_hint=(None, None), size=(400, 200))
        popup.open()

    def on_confirm_button_press(self, cantidad, producto, popup):
        cantidad = int(cantidad)
        self.on_enter(cantidad, producto)
        # Cierra la ventana emergente después de procesar la cantidad ingresada
        popup.dismiss()

    def on_enter(self, cantidad, producto):
        # Maneja la entrada de cantidad
        total_producto = cantidad * producto._precio

        # Actualiza el carrito y el total
        self.carrito.append({"nombre": producto._nombre, "cantidad": cantidad, "total": total_producto})
        self.total += total_producto

        # Actualiza el texto del botón de total
        self.total_button.text = f"Total: ${self.total}"

        # Actualiza la interfaz gráfica para mostrar el carrito
        self.update_carrito()

    def update_carrito(self):
        # Limpia el layout del carrito
        self.layout_carrito_content.clear_widgets()

        # Muestra el carrito
        for item in self.carrito:
            btn = Button(text=f"- {item['nombre']}s x {item['cantidad']}u. a ${item['total']}", size_hint=(1, None), height=40,
                          background_color=(0.5, 0, 0, 1))  # Cambia el color de fondo
            btn.item = item
            btn.bind(on_press=self.remove_from_cart)
            self.layout_carrito_content.add_widget(btn)

    def remove_from_cart(self, instance):
        item = instance.item
        self.total -= item['total']
        self.total_button.text = f"Total: ${self.total}"
        self.carrito.remove(item)
        self.update_carrito()

    def show_total_popup(self, instance):
        # Muestra un popup con el total actual
        total_popup = Popup(title='Total', content=Button(text=f"Total: ${self.total}"), size_hint=(None, None),
                            size=(200, 100))
        total_popup.open()

if __name__ == "__main__":
    PedidoApp().run()
