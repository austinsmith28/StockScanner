from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget

Builder.load_file('guiMain.kv')


class Screen(Widget):
    pass


class Main(App):
    def build(self):
        return Screen()


if __name__ == '__main__':
    Main().run()
