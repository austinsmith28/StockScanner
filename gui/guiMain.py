import main
from threading import Thread
from displayMain import Display
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget

Builder.load_file('guiMain.kv')

tlist = {}
display = Widget

class Screen(Widget):

    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        global display
        display = self.ids.display

    @staticmethod
    def set_list(list):
        global tlist
        tlist = list
        t1 = Thread(target=Screen.buildDisplayPanel, args=[display])
        t2 = Thread(target=Screen.getPrices)
        t1.start()
        t2.start()

    @staticmethod
    def getPrices():
        plist = main.get_prices(tlist)
        print(plist)


    # build display panel
    def buildDisplayPanel(self):
        Display.build(self, tlist)

class Main(App):
    def build(self):
        return Screen()


if __name__ == '__main__':
    Main().run()
