from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('displayMain.kv')


class Display(BoxLayout):
    pass


class Main(App):
    def build(self):
        return Display()


if __name__ == '__main__':
    Main().run()
