from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.text_input = TextInput(hint_text='Qui comparirà il messaggio', font_size=24)
        button = Button(text='Scrivi Ciao mondo', font_size=24)
        button.bind(on_press=self.scrivi_ciao)

        layout.add_widget(self.text_input)
        layout.add_widget(button)

        return layout

    def scrivi_ciao(self, instance):
        self.text_input.text = 'Ciao mondo'

if __name__ == '__main__':
    MyApp().run()
