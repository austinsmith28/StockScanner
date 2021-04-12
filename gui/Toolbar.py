from kivy.app import App
from kivy.lang import Builder
from kivy.uix.spinner import Spinner
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
import main

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

            "price_low": fundamentals.price_low.text,
            "price_high": fundamentals.price_high.text,
            "vol_low": fundamentals.volume_low.text,
            "vol_high": fundamentals.volume_high.text,
            "mktcap_low": fundamentals.mktcap_low.text,
            "mktcap_high": fundamentals.mktcap_high.text,
            "share_low": fundamentals.share_low.text,
            "share_high": fundamentals.share_high.text,
            "short_low": fundamentals.short_low.text,
            "short_high": fundamentals.short_high.text,
            "change_low": fundamentals.change_low.text,
            "change_high": fundamentals.change_high.text,

            "timeperiod": technical.timeperiod.text,
            "indicator": technical.indicator.text,
            "threshold": technical.threshold.text
        }

        return main.search(dict)


class Main(App):
    def build(self):
        return Toolbar()


if __name__ == '__main__':
    Main().run()
