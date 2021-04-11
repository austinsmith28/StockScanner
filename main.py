# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import requests
import bs4

import json
import pandas as pd

api_key = 'ddca75d268744b19b3cb78676aab6c54'


def no_numbers(input_string):
    return not any(char.isdigit() for char in input_string)


def remove_duplicates(array):
    res = []
    for name in array:
        if name not in res:
            res.append(name)
    return res


def str_value_to_num(input_value):
    output = input_value

    if input_value[-1] == "T":
        output = input_value[:-1]
        output.replace(".", "")
        output = float(output)
        output = output * 1000000000000  # Trillion

    if input_value[-1] == "B":
        output = input_value[:-1]
        output.replace(".", "")
        output = float(output)
        output = output * 1000000000  # Billion

    if input_value[-1] == "M":
        output = input_value[:-1]
        output.replace(".", "")
        output = float(output)
        output = output * 1000000  # Million

    return output


def remove_commas(input_val):
    return input_val.replace(",", "")


def price_bounds(lower, upper, array):
    res = []
    url = "https://finviz.com/quote.ashx?t="

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/68.0.3440.106 Safari/537.36', }
    for i in array:

        full_url = url + i

        response = requests.get(full_url, headers=headers).content

        soup = bs4.BeautifulSoup(response, 'html.parser')
        try:
            # stock_price = soup.body.find('span', class_="C($primaryColor) Fz(24px) Fw(b)").text

            # stock_price = soup.body.find('span', class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)").text
            stock_price = soup.find("td", text="Price").find_next_sibling("td").text
            # print("price of " , i, " is ", stock_price)
            float_stock_price = float(stock_price)

            if lower <= float_stock_price <= upper:
                res.append(i)
                print(i, " price is ", stock_price)
        except AttributeError:
            print("stock is ", i)

        '''
        price_url = f'https://api.twelvedata.com/price?symbol={i}&apikey={api_key}'
        stock_price_request = requests.get(price_url).json()

        try:
            stock_price = stock_price_request['price']
        except KeyError:
            stock_price = -1

        print(i, stock_price)
        float_stock_price = float(stock_price)

        if lower <= float_stock_price <= upper:
            res.append(i)
        '''
    return res


def volume_bounds(lower, upper, array):
    res = []
    url = "https://finviz.com/quote.ashx?t="

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/68.0.3440.106 Safari/537.36', }
    for i in array:

        full_url = url + i

        response = requests.get(full_url, headers=headers).content

        soup = bs4.BeautifulSoup(response, 'html.parser')
        try:
            stock_volume = soup.find("td", text="Volume").find_next_sibling("td").text

            float_stock_volume = remove_commas(stock_volume)

            float_stock_volume = float(float_stock_volume)

            if lower <= float_stock_volume <= upper:
                res.append(i)
                print(i, " price is ", stock_volume)
        except AttributeError:
            print("stock is ", i)
    return res


def market_cap_bounds(lower, upper, array):
    res = []
    url = "https://finviz.com/quote.ashx?t="

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/68.0.3440.106 Safari/537.36', }
    for i in array:

        full_url = url + i

        response = requests.get(full_url, headers=headers).content

        soup = bs4.BeautifulSoup(response, 'html.parser')
        try:
            market_cap = soup.find("td", text="Market Cap").find_next_sibling("td").text
            market_cap = str_value_to_num(market_cap)

            if lower <= market_cap <= upper:
                res.append(i)
                print(i, " market cap is ", market_cap)
        except AttributeError:
            print("stock is ", i)
    return res


def share_float_bounds(lower, upper, array):
    res = []
    url = "https://finviz.com/quote.ashx?t="

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/68.0.3440.106 Safari/537.36', }
    for i in array:

        full_url = url + i

        response = requests.get(full_url, headers=headers).content

        soup = bs4.BeautifulSoup(response, 'html.parser')
        try:
            share_float = soup.find("td", text="Shs Float").find_next_sibling("td").text
            share_float = str_value_to_num(share_float)

            if lower <= share_float <= upper:
                res.append(i)
                print(i, " share float is ", share_float)
        except AttributeError:
            print("stock is ", i)

    return res


def short_float_bounds(lower, upper, array):
    res = []
    url = "https://finviz.com/quote.ashx?t="

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/68.0.3440.106 Safari/537.36', }
    for i in array:

        full_url = url + i

        response = requests.get(full_url, headers=headers).content

        soup = bs4.BeautifulSoup(response, 'html.parser')
        try:
            short_float = soup.find("td", text="Short Float").find_next_sibling("td").text
            short_float = short_float[:-1]

            if lower <= short_float <= upper:
                res.append(i)
                print(i, " short float is ", short_float)
        except AttributeError:
            print("stock is ", i)

    return res


def daily_change_percent(lower, upper, array):
    res = []
    url = "https://finviz.com/quote.ashx?t="

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/68.0.3440.106 Safari/537.36', }
    for i in array:

        full_url = url + i

        response = requests.get(full_url, headers=headers).content

        soup = bs4.BeautifulSoup(response, 'html.parser')
        try:
            change = soup.find("td", text="Change").find_next_sibling("td").text
            change = change[:-1]

            if lower <= change <= upper:
                res.append(i)
                print(i, " change is ", change)
        except AttributeError:
            print("stock is ", i)

    return res


# interval = input("Enter a Time Interval:")
# technical = input("Enter a Technical Indicator:")


################################################################
#       CURRENTLY RUNNING AS A SCRIPT BUT THE BELOW CODE       #
#       WILL EVENTUALLY BE ITS OWN FUNCTION TO CONNECT         #
#       BACK-END WITH THE FRONT-END                            #
################################################################

def search(search_dict):

    asset = search_dict['asset']

    vol_low = search_dict['vol_low']
    vol_high = search_dict['vol_high']

    mktcap_low = search_dict['mktcap_low']
    mktcap_high = search_dict['mktcap_high']

    c

    return


allStocksUrl = f'https://api.twelvedata.com/stocks'

allStockData = requests.get(allStocksUrl).json()

allSymbols = []

for i in allStockData['data']:
    if no_numbers(i['symbol']) and i['type'] == "Common Stock" and (
            i['exchange'] == "NASDAQ" or i[
        'exchange'] == "NYSE"):  ###TODO: FIX HARD CODED STRING "COMMON STOCK" and exchanges
        allSymbols.append(i['symbol'])
print(len(allSymbols))
newSymbols = remove_duplicates(allSymbols)

price_bound_symbols = price_bounds(5, 10, newSymbols)  # TODO: FIX HARD CODED UPPER AND LOWER PRICE BOUNDS

print(price_bound_symbols)

'''
for ticker in allSymbols:
    counter = 0
    api_url = f'https://api.twelvedata.com/{technical}?symbol={ticker}&interval={interval}&outputsize=12&apikey={api_key}'
    data = requests.get(api_url).json()


for j in data['meta']:
    print(j['symbol'])


'''
