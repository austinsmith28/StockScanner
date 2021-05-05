import main
import time
from guiMain import Screen
from kivy.lang import Builder
from kivy.uix.spinner import Spinner
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from threading import Thread

Builder.load_file('Toolbar.kv')

class Header(GridLayout):
    pass
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

    #create thread to prevent program from lagging
    def search(self):
        t1 = Thread(target=Toolbar.build_list, args=[self])
        t1.start()
        return

    #builds and returns the dictionary to be sent to backend
    def build_dict(self):
        time1 = time.time_ns()

        fundamentals = self.ids.fundamentals.ids
        technical = self.ids.technical.ids

        # dict to send to api
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

    #use dictionary to create the stock list
    def build_list(self):

        #set the dictionary values
        tool_dict = Toolbar.build_dict(self)

        #set the list based on dictionary values
        time1 = time.time()
        tool_list = main.search(tool_dict)
        time2 = time.time()
        print("Function return time: " + str(time2 - time1) + " s")

        print(tool_list)

        #send list back to the main function
        Screen.set_list(tool_list)

