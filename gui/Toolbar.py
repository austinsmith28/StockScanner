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

        fundamentals = self.ids.fundamentals.ids
        technical = self.ids.technical.ids

        dict = {
            "asset": self.ids.asset.text,

            "vol_low": fundamentals.volume_low.text,
            "vol_high": fundamentals.volume_high.text,
            "mktcap_low": fundamentals.mktcap_low.text,
            "mktcap_high": fundamentals.mktcap_high.text,
            "change_low": fundamentals.change_low.text,
            "change_high": fundamentals.change_high.text,

            "timeperiod": technical.timeperiod.text,
            "indicator": technical.indicator.text,
            "threshold": technical.threshold.text
        }


class Main(App):
    def build(self):
        return Toolbar()


if __name__ == '__main__':
    Main().run()
