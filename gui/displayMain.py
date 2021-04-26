from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget

Builder.load_file('displayMain.kv')

display = Widget

class Display(BoxLayout):

    def __init__(self, **kwargs):
        super(Display, self).__init__(**kwargs)
        global display
        display = self

    def build(self, tlist):
        x = 0
        print("blubber boy")
        for i in tlist:
            x += 1
            display.add_widget(Label(text=i))
            if x == 25:
                break
        return self


class Main(App):
    def build(self):
        return Display()


if __name__ == '__main__':
    Main().run()
