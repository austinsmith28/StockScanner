# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import requests
import json
import pandas as pd

api_key = 'ddca75d268744b19b3cb78676aab6c54'


def search(asset_class, price, moving_average_period, indicator, threshold):

    return


def no_numbers(input_string):
    return not any(char.isdigit() for char in input_string)


def remove_duplicates(array):
    res = []
    for name in array:
        if name not in res:
            res.append(name)
    return res


def price_bounds(lower, upper, array):
    res = []
    for i in array:
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

    return res






#interval = input("Enter a Time Interval:")
#technical = input("Enter a Technical Indicator:")



allStocksUrl = f'https://api.twelvedata.com/stocks'

allStockData = requests.get(allStocksUrl).json()

allSymbols = []

for i in allStockData['data']:
    if no_numbers(i['symbol']) and i['type'] == "Common Stock": ###TODO: FIX HARD CODED STRING "COMMON STOCK"
        allSymbols.append(i['symbol'])

newSymbols = remove_duplicates(allSymbols)

price_bound_symbols = price_bounds(5, 10, newSymbols) #TODO: FIX HARD CODED UPPER AND LOWER PRICE BOUNDS

print(price_bound_symbols)



'''
for ticker in allSymbols:
    counter = 0
    api_url = f'https://api.twelvedata.com/{technical}?symbol={ticker}&interval={interval}&outputsize=12&apikey={api_key}'
    data = requests.get(api_url).json()


for j in data['meta']:
    print(j['symbol'])


'''