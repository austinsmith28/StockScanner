from kivy.uix.boxlayout import BoxLayout

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.spinner import Spinner
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget

# mess of attempt at just a simple calculation page
#toolbar.kv spacing pos_hint: {"top": .#-.1}

Builder.load_file('calc.kv')
class Header(RelativeLayout):
    pass
class TimeRange(Spinner):
    pass
class calc(GridLayout):
    pass

class Calc(App):
    def build(self):
        return calc()

if __name__ == '__main__':
    Calc().run()
