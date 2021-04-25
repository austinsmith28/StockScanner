from kivy.app import App
from kivy.lang import Builder

Builder.load_file('displayMain.kv')


class Display():
    pass

class Main(App):
    def build(self):
        return


if __name__ == '__main__':
    Main().run()
