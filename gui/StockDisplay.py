import guiMain
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

Builder.load_file('StockDisplay.kv')


class StockDisplay(BoxLayout):
    def build(self, tlist):
        for i in tlist:
            lbl = Label(text=i)
            self.add_widget(lbl)
        return guiMain.Screen()


class Main(App):
    def build(self):
        return StockDisplay()

if __name__ == '__main__':
    Main().run()
