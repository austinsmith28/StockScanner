# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import requests
from bs4 import BeautifulSoup, SoupStrainer
import lxml

import json
import pandas as pd

api_key = 'ddca75d268744b19b3cb78676aab6c54'

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(
    pool_connections=100,
    pool_maxsize=100)
session.mount('https://', adapter)


def only_letters(input_string):
    return any(char.isalpha() for char in input_string)


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
    counter = 0
    res = []
    url = "https://finviz.com/quote.ashx?t="

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/68.0.3440.106 Safari/537.36', }
    for i in array:

        full_url = url + i

        response = session.get(full_url, headers=headers).content
        strainer = SoupStrainer('table', class_="snapshot-table2")
        soup = BeautifulSoup(response, 'lxml', parse_only=strainer)
        try:
            # stock_price = soup.body.find('span', class_="C($primaryColor) Fz(24px) Fw(b)").text

            # stock_price = soup.body.find('span', class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)").text
            stock_price = soup.find("td", text="Price").find_next_sibling("td").text
            # print("price of " , i, " is ", stock_price)
            float_stock_price = float(stock_price)
            print(counter)
            counter += 1
            if lower <= float_stock_price <= upper:
                res.append(i)
                # print(i, " price is ", stock_price)
        except AttributeError:
            # print("stock is ", i)
            pass

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

        response = session.get(full_url, headers=headers).content
        strainer = SoupStrainer('table', class_="snapshot-table2")
        soup = BeautifulSoup(response, 'lxml', parse_only=strainer)

        try:
            stock_volume = soup.find("td", text="Volume").find_next_sibling("td").text

            float_stock_volume = remove_commas(stock_volume)

            float_stock_volume = float(float_stock_volume)

            if lower <= float_stock_volume <= upper:
                res.append(i)
                print(i, " volume is ", stock_volume)
        except AttributeError:
            # print("stock is ", i)
            pass
    return res


def market_cap_bounds(lower, upper, array):
    res = []
    url = "https://finviz.com/quote.ashx?t="

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/68.0.3440.106 Safari/537.36', }
    for i in array:

        full_url = url + i

        response = session.get(full_url, headers=headers).content
        strainer = SoupStrainer('table', class_="snapshot-table2")
        soup = BeautifulSoup(response, 'lxml', parse_only=strainer)

        try:
            market_cap = soup.find("td", text="Market Cap").find_next_sibling("td").text
            market_cap = str_value_to_num(market_cap)

            if lower <= market_cap <= upper:
                res.append(i)
                # print(i, " market cap is ", market_cap)
        except AttributeError:
            # print("stock is ", i)
            pass
    return res


def share_float_bounds(lower, upper, array):
    res = []
    url = "https://finviz.com/quote.ashx?t="

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/68.0.3440.106 Safari/537.36', }
    for i in array:
        # print('Trying ',i)
        full_url = url + i

        response = session.get(full_url, headers=headers).content
        strainer = SoupStrainer('table', class_="snapshot-table2")
        soup = BeautifulSoup(response, 'lxml', parse_only=strainer)

        try:
            share_float = soup.find("td", text="Shs Float").find_next_sibling("td").text
            share_float = str_value_to_num(share_float)

            if share_float != "-" and lower <= share_float <= upper:
                res.append(i)
                # print(i, " share float is ", share_float)
        except AttributeError:
            # print("stock is ", i)
            pass
    return res


def short_float_bounds(lower, upper, array):
    res = []
    url = "https://finviz.com/quote.ashx?t="

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/68.0.3440.106 Safari/537.36', }
    for i in array:

        full_url = url + i

        response = session.get(full_url, headers=headers).content
        strainer = SoupStrainer('table', class_="snapshot-table2")
        soup = BeautifulSoup(response, 'lxml', parse_only=strainer)

        try:
            short_float = soup.find("td", text="Short Float").find_next_sibling("td").text
            short_float = short_float[:-1]

            if lower <= short_float <= upper:
                res.append(i)
                # print(i, " short float is ", short_float)
        except AttributeError:
            # print("stock is ", i)
            pass

    return res


def daily_change_percent(lower, upper, array):
    res = []
    url = "https://finviz.com/quote.ashx?t="

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/68.0.3440.106 Safari/537.36', }
    for i in array:

        full_url = url + i

        response = session.get(full_url, headers=headers).content
        strainer = SoupStrainer('table', class_="snapshot-table2")
        soup = BeautifulSoup(response, 'lxml', parse_only=strainer)

        try:
            change = soup.find("td", text="Change").find_next_sibling("td").text
            change = float(change[:-1])

            if lower <= change <= upper:
                res.append(i)
                # print(i, " change is ", change)
        except AttributeError:
            # print("stock is ", i)
            pass

    return res


def moving_averages(indicator, interval, time_period, threshold, array):
    res = []
    for i in array:
        url = f"https://api.twelvedata.com/{indicator}?symbol={i}&interval={interval}&time_period={time_period}&apikey={api_key} "
        indicator_request = requests.get(url).json()

        price_url = f'https://api.twelvedata.com/price?symbol={i}&apikey={api_key}'
        stock_price_request = requests.get(price_url).json()
        try:
            stock_price = float(stock_price_request['price'])
            indicator_price = float(indicator_request['values'][0][indicator])

            threshold = threshold * .01

            lower_threshold = stock_price * (1 - threshold)
            upper_threshold = stock_price * (1 + threshold)

            if lower_threshold <= indicator_price <= upper_threshold:
                res.append(i)

        except AttributeError:
            pass

    return res


def get_stocks():
    all_stocks_url = f'https://api.twelvedata.com/stocks'

    all_stock_data = requests.get(all_stocks_url).json()

    all_symbols = []

    for i in all_stock_data['data']:
        if only_letters(i['symbol']) and (i['exchange'] == "NASDAQ" or i['exchange'] == "NYSE") and i[
            'type'] == "Common Stock":
            all_symbols.append(i['symbol'])

    new_symbols = remove_duplicates(all_symbols)
    # print(len(new_symbols))
    return new_symbols


################################################################
#       CURRENTLY RUNNING AS A SCRIPT BUT THE BELOW CODE       #
#       WILL EVENTUALLY BE ITS OWN FUNCTION TO CONNECT         #
#       BACK-END WITH THE FRONT-END                            #
################################################################

def search(search_dict):
    asset = search_dict['asset']

    symbols = get_stocks()

    if search_dict['price_low'] != "" and search_dict['price_high'] != "":
        price_low = float(search_dict['price_low'])
        price_high = float(search_dict['price_high'])
        symbols = price_bounds(price_low, price_high, symbols)

    if search_dict['vol_low'] != "" and search_dict['vol_high'] != "":
        vol_low = float(search_dict['vol_low'])
        vol_high = float(search_dict['vol_high'])
        symbols = volume_bounds(vol_low, vol_high, symbols)

    if search_dict['share_low'] != "" and search_dict['share_high'] != "":
        share_float_low = float(search_dict['share_low'])
        share_float_high = float(search_dict['share_high'])
        symbols = share_float_bounds(share_float_low, share_float_high, symbols)

    if search_dict['short_low'] != "" and search_dict['short_high'] != "":
        short_float_low = float(search_dict['short_low'])
        short_float_high = float(search_dict['short_high'])
        symbols = short_float_bounds(short_float_low, short_float_high, symbols)

    if search_dict['mktcap_low'] != "" and search_dict['mktcap_high'] != "":
        mktcap_low = float(search_dict['mktcap_low'])
        mktcap_high = float(search_dict['mktcap_high'])
        symbols = market_cap_bounds(mktcap_low, mktcap_high, symbols)

    if search_dict['change_low'] != "" and search_dict['change_high'] != "":
        change_low = float(search_dict['change_low'])
        change_high = float(search_dict['change_high'])
        symbols = daily_change_percent(change_low, change_high, symbols)

    if search_dict['timeperiod'] != "" and search_dict['indicator'] != "" and search_dict['threshold'] != "" and \
            search_dict['interval'] != "":
        timeperiod = float(search_dict['timeperiod'])
        indicator = search_dict['indicator']
        indicator_threshold = float(search_dict['threshold'])
        interval = search_dict['interval']

        symbols = moving_averages(indicator, interval, timeperiod, indicator_threshold, symbols)

    return_dict = []

    # print(float_bound_symbols)

    return symbols
