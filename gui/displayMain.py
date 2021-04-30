from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget

Builder.load_file('displayMain.kv')

display = Widget
tlist ={}
p = 0

class Display(BoxLayout):

    def __init__(self, **kwargs):
        super(Display, self).__init__(**kwargs)
        global display
        display = self

    def build(self, list):
        x = 0
        display.clear_widgets()
        global tlist
        global p
        tlist = list
        p = 0
        print("blubber boy")

        for i in range(24):
            display.add_widget(Label(text=tlist[i]))
        display.add_widget(Button(text="next", on_release=Display.next(self)))

        return self

    def next(self):
        print("beotch")
        display.clear_widgets()
        global p
        p = p + 1
        for i in range(24):
            display.add_widget(Label(text=tlist[i + (p * 24)]))
        display.add_widget(Button())



class Main(App):
    def build(self):
        return Display()


if __name__ == '__main__':
    Main().run()
