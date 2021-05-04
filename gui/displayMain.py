from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget

Builder.load_file('displayMain.kv')

# global variables
display = Widget
tlist = []
dislist= []
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

        Display.fillPanel(self, page)

        return self


    def addPrices(self, plist):
        for i in range(disp_len):
            dislist[i].text = dislist[i].text + str(".......") + plist[i + (page * disp_len)]


    # fill display panel contents
    def fillPanel(self, p):

        global dislist

        for i in range(disp_len):
            i = DisplayLabel(text=tlist[i + (p * disp_len)])
            dislist.append(i)
            display.add_widget(i)
        print(dislist)

        # build previous button
        display.submit = Button(text="previous")
        display.submit.bind(on_release=display.previous)
        display.add_widget(display.submit)

        # build next button
        display.submit = Button(text="next")
        display.submit.bind(on_release=display.next)
        display.add_widget(display.submit)

    # go to last page
    def previous(self, instance):

        global page

        # check if page can go back
        if page > 0:
            page = page - 1
            print("page " + str(page))
            display.clear_widgets()
            Display.fillPanel(self, page)
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
            Display.fillPanel(self, page)
        else:
            print("on last page")

# initialize label widget
class DisplayLabel(Label):
    pass

