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
cap = 1

class Display(BoxLayout):

    def __init__(self, **kwargs):
        super(Display, self).__init__(**kwargs)
        global display
        display = self

    def build(self, list):
        global tlist
        global p
        global cap
        display.clear_widgets()

        tlist = list
        p = 0

        while len(tlist) % 24 != 0:
            tlist.append("")

        cap = len(tlist) / 24

        print("blubber boy")

        Display.ihatethis(self, p)

        return self

    def ihatethis(self, p):
        for i in range(24):
            display.add_widget(DisplayLabel(text=tlist[i + (p * 24)]))

        display.submit = Button(text="previous")
        display.submit.bind(on_release=display.previous)
        display.add_widget(display.submit)

        display.submit = Button(text="next")
        display.submit.bind(on_release=display.next)
        display.add_widget(display.submit)

    def previous(self, instance):
        print("the last beotch")
        global p
        global cap

        if p > 0:
            p = p - 1
            display.clear_widgets()
            Display.ihatethis(self, p)
        else:
            print("ur dad")

    def next(self, instance):
        print("the next beotch")
        global p
        global cap

        if p < cap:
            p = p + 1
            display.clear_widgets()
            Display.ihatethis(self, p)
        else:
            print("ur mom")

class DisplayLabel(Label):
    pass

class Main(App):
    def build(self):
        return Display()


if __name__ == '__main__':
    Main().run()
