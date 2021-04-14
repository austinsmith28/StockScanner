import queue

from kivy.uix.boxlayout import BoxLayout

import main
import time
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.spinner import Spinner
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from threading import Thread

Builder.load_file('Toolbar.kv')

class AssetType(Spinner):
    pass
class Fundamentals(GridLayout):
    pass
class Interval(Spinner):
    pass
class Indicator(Spinner):
    pass
class Technical(GridLayout):
    pass

class Toolbar(Widget):

    def search(self):
        t1 = Thread(target=Toolbar.build_thread, args=[self])
        t1.start()
        return

    def build_dict(self):
        time1 = time.time_ns()

        fundamentals = self.ids.fundamentals.ids
        technical = self.ids.technical.ids

        tool_dict = {
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
            "interval": technical.interval.text,
            "indicator": technical.indicator.text,
            "threshold": technical.threshold.text
        }

        time2 = time.time_ns()
        print("Dictionary build time: " + str(time2 - time1) + " ns")
        return tool_dict

    def build_thread(self):

        tool_dict = Toolbar.build_dict(self)
        time1 = time.time()
        tool_list = main.search(tool_dict)
        time2 = time.time()
        print("Function return time: " + str(time2 - time1) + " s")
        print(tool_list)

class Main(App):
    def build(self):
        return Toolbar()


if __name__ == '__main__':
    Main().run()
