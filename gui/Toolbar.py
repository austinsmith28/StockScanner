from kivy.app import App
from kivy.lang import Builder
from kivy.uix.spinner import Spinner
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget

Builder.load_file('Toolbar.kv')


class Technical(GridLayout):
    pass


class Fundamentals(GridLayout):
    pass


class AssetType(Spinner):
    pass


class Indicator(Spinner):
    pass


class Toolbar(Widget):
    def search(self):
        pass


class Main(App):
    def build(self):
        return Toolbar()


if __name__ == '__main__':
    Main().run()
