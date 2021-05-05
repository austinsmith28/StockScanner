from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget

import main
from gui import stockPrices

Builder.load_file('displayMain.kv')

# global variables
display = Widget
tlist = []          # list of stock names
plist = []          # list of prices
dislist= []         # list of memory locations of labels
page = 0
cap = 1
disp_len = 24

# initialize display panel
class Display(BoxLayout):

    # define reference to display widget
    def __init__(self, **kwargs):
        super(Display, self).__init__(**kwargs)
        global display
        display = self

    # build display panel
    def build(self, list):
        global tlist
        global page
        global cap

        # set global values
        display.clear_widgets()
        tlist = list
        page = 0

        # ensure that list is divisible by display length
        while len(tlist) % disp_len != 0:
            tlist.append("")

        cap = len(tlist) / disp_len

        # cheeky debug note
        print("blubber boy")

        Display.fillPanel(self)

        return self

    # fill display panel contents
    def fillPanel(self):

        global dislist
        global plist

        p = page * disp_len
        plist = stockPrices.getPrices(tlist[p:p + disp_len])

        for i in range(disp_len):
            i = DisplayLabel(text=(str(tlist[i + p]) + str("..........") + str(plist[i])))
            dislist.append(i)
            display.add_widget(i)
        print(dislist)

        fl = FloatLayout()
        display.add_widget(fl)

        # build previous button
        fl.submit = Button(text="previous", size_hint=(.5, 1), pos_hint={'x': 0})
        fl.submit.bind(on_release=display.previous)
        fl.add_widget(fl.submit)

        # build next button
        fl.submit = Button(text="next", size_hint=(.5, 1), pos_hint={'x': .5})
        fl.submit.bind(on_release=display.next)
        fl.add_widget(fl.submit)

    # go to last page
    def previous(self, instance):

        global page

        # check if page can go back
        if page > 0:
            page = page - 1
            print("page " + str(page))
            display.clear_widgets()
            Display.fillPanel(self)
        else:
            print("on first page")

    # go to next page
    def next(self, instance):

        global page

        # check if page can go forward
        if (page + 1) < cap:
            page = page + 1
            print("page " + str(page))
            display.clear_widgets()
            Display.fillPanel(self)
        else:
            print("on last page")

# initialize label widget
class DisplayLabel(Label):
    pass

