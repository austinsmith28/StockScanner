# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import requests
from bs4 import BeautifulSoup, SoupStrainer
import time

api_key = 'ddca75d268744b19b3cb78676aab6c54'

# Creating Open Session so HTTP requests do not create a new session each time a request is made.
session = requests.Session()
adapter = requests.adapters.HTTPAdapter(
    pool_connections=100,
    pool_maxsize=100)
session.mount('https://', adapter)

"""
Determines if a string contains only letters (A-z)

Args:
    input_string::str
        The string to evaluate

Returns:
    bool::bool
        True if input_string only contains characters (A-z); else returns false
"""
def only_letters(input_string):
    return any(char.isalpha() for char in input_string)


"""
Removes duplicate elements from an array

Args:
    array::array
        The array to evaluate

Returns:
    res::array
        An array that has no duplicate elements
"""
def remove_duplicates(array):
    res = []
    for name in array:
        if name not in res:
            res.append(name)
    return res


"""
Converts string value returned from finviz that is postfaced with an alpha to a float value
ex: 1.7M = 1,700,000 million = 1700000

Args:
    input_string::str
        The string to evaluate

Returns:
    output::float
        True if input_string only contains characters (A-z); else returns false
"""
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


"""
Remove commas from input string

Args:
    input_val::str
        The string to remove commas from

Returns:
    str::str
        input_val with commas replaced as ""
"""
def remove_commas(input_val):
    return input_val.replace(",", "")


"""
Determines stocks that are within users price criteria

Args:
    lower::float
        minimum price
    upper::float
        maximum price
    array:array
        array of stock tickers to be evaluated

Returns:
    res::array
        the resulting stock tickers left after being bound to user price criteria
        
"""
def price_bounds(lower, upper, array):
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
            stock_price = soup.find("td", text="Price").find_next_sibling("td").text
            float_stock_price = float(stock_price)

            if lower <= float_stock_price <= upper:
                res.append(i)

        except AttributeError:
            print("AttributeError on ", i)
            pass

    return res


"""
Determines stocks that are within users volume criteria

Args:
    lower::float
        minimum volume
    upper::float
        maximum volume
    array:array
        array of stock tickers to be evaluated

Returns:
    res::array
        the resulting stock tickers left after being bound to user volume criteria

"""
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

        except AttributeError:
            print("AttributeError on ", i)
            pass

    return res


"""
Determines stocks that are within users market capitalization criteria

Args:
    lower::float
        minimum market capitalization range
    upper::float
        maximum market capitalization range
    array:array
        array of stock tickers to be evaluated

Returns:
    res::array
        the resulting stock tickers left after being bound to user market capitalization criteria

"""
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
            remove_commas(market_cap)
            market_cap = str_value_to_num(market_cap)
            if market_cap != "-":
                market_cap = float(market_cap)

            if market_cap != "-" and lower <= market_cap <= upper:
                res.append(i)

        except AttributeError:
            print("AttributeError on ", i)
            pass

    return res


"""
Determines stocks that are within users share float criteria

Args:
    lower::float
        minimum share float range
    upper::float
        maximum share float range
    array:array
        array of stock tickers to be evaluated

Returns:
    res::array
        the resulting stock tickers left after being bound to user market capitalization criteria

"""
def share_float_bounds(lower, upper, array):
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
            share_float = soup.find("td", text="Shs Float").find_next_sibling("td").text
            share_float = str_value_to_num(share_float)
            if share_float != "-":
                share_float = float(share_float)
            if share_float != "-" and lower <= share_float <= upper:
                res.append(i)

        except AttributeError:
            print("AttributeError on ", i)
            pass

    return res


"""
Determines stocks that are within users short float criteria

Args:
    lower::float
        minimum short float range
    upper::float
        maximum short float range
    array:array
        array of stock tickers to be evaluated

Returns:
    res::array
        the resulting stock tickers left after being bound to user short float criteria

"""
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
            if short_float != "-":
                short_float = float(short_float[:-1])

            if short_float != "-" and lower <= short_float <= upper:
                res.append(i)

        except AttributeError:
            print("AttributeError on ", i)
            pass

    return res


"""
Determines stocks that are within users daily percentage change criteria

Args:
    lower::float
        minimum percent change
    upper::float
        maximum percent change
    array:array
        array of stock tickers to be evaluated

Returns:
    res::array
        the resulting stock tickers left after being bound to user daily change percent criteria

"""
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

        except AttributeError:
            print("AttributeError on ", i)
            pass
    return res


"""
Determines stocks that are priced within a certain percent of a moving average price

Args:
    indicator::str
        the technical indicator the user would like to use
    interval::str
        time frame of the moving average to be calculated on
    time_period::int
        the amount of intervals to be used when calculating the average (1-800)
    threshold::float
        percent value to require moving average to be within compared to stock price

Returns:
    res::array
        the resulting stock tickers left after being bound to user moving average criteria

"""
def moving_averages(indicator, interval, time_period, threshold, array):
    res = []
    counter = 1
    threshold = threshold * .01

    for i in array:

        if counter % 27 == 0:
            print("pausing for 1 minute due to API restrictions")
            time.sleep(61)

        url = f"https://api.twelvedata.com/{indicator}?symbol={i}&interval={interval}&time_period={time_period}&apikey={api_key}"

        indicator_request = requests.get(url).json()

        price_url = f'https://api.twelvedata.com/price?symbol={i}&apikey={api_key}'
        stock_price_request = requests.get(price_url).json()

        try:

            stock_price = float(stock_price_request['price'])
            indicator_price = float(indicator_request['values'][0][indicator])

            lower_threshold = stock_price * (1 - threshold)
            upper_threshold = stock_price * (1 + threshold)

            if lower_threshold <= indicator_price <= upper_threshold:
                res.append(i)

        except KeyError:
            print('key error on ', i)
            pass

        counter += 1
    return res


"""
Creates the initial array of all available stock tickers found on TwelveData

Args:
    NONE

Returns:
    new_symbols::array
        the resulting array of all stock tickers excluding duplicates and non-alpha elements

"""
def get_stocks():
    all_stocks_url = f'https://api.twelvedata.com/stocks'

    all_stock_data = requests.get(all_stocks_url).json()

    all_symbols = []

    for i in all_stock_data['data']:
        if only_letters(i['symbol']) and (
                i['exchange'] == "NASDAQ" or i['exchange'] == "NYSE" or i['exchange'] == "AMEX") and i[
            'type'] == "Common Stock":
            all_symbols.append(i['symbol'])

    new_symbols = remove_duplicates(all_symbols)
    # print(len(new_symbols))
    return new_symbols


################################################################
#     code below is the function that the front end calls      #
################################################################

"""
Think of this as the main function. The front-end will call this function when a user wants to search
for stocks based on their criteria entered on the front-end GUI. 

Args:
    search_dict::dict

Returns:
    symbols::array
        the resulting stock tickers left after being bound to ALL of the users criteria provided
"""
def search(search_dict):
    asset = search_dict['asset']

    symbols = get_stocks()

    if search_dict['price_low'] != "" and search_dict['price_high'] != "":
        print("starting price func")

        price_low = float(search_dict['price_low'])
        price_high = float(search_dict['price_high'])
        symbols = price_bounds(price_low, price_high, symbols)

    if search_dict['vol_low'] != "" and search_dict['vol_high'] != "":
        print("starting vol func")

        vol_low = float(search_dict['vol_low'])
        vol_high = float(search_dict['vol_high'])
        symbols = volume_bounds(vol_low, vol_high, symbols)

    if search_dict['share_low'] != "" and search_dict['share_high'] != "":
        print("starting float func")

        share_float_low = float(search_dict['share_low'])
        share_float_high = float(search_dict['share_high'])
        symbols = share_float_bounds(share_float_low, share_float_high, symbols)

    if search_dict['short_low'] != "" and search_dict['short_high'] != "":
        print("starting short func")

        short_float_low = float(search_dict['short_low'])
        short_float_high = float(search_dict['short_high'])
        symbols = short_float_bounds(short_float_low, short_float_high, symbols)

    if search_dict['mktcap_low'] != "" and search_dict['mktcap_high'] != "":
        print("starting marketcap func")

        mktcap_low = float(search_dict['mktcap_low'])
        mktcap_high = float(search_dict['mktcap_high'])
        symbols = market_cap_bounds(mktcap_low, mktcap_high, symbols)

    if search_dict['change_low'] != "" and search_dict['change_high'] != "":
        print("starting change func")

        change_low = float(search_dict['change_low'])
        change_high = float(search_dict['change_high'])
        symbols = daily_change_percent(change_low, change_high, symbols)

    if search_dict['timeperiod'] != "" and search_dict['indicator'] != "" and search_dict['threshold'] != "" and \
            search_dict['interval'] != "":
        print("starting technicals func")

        timeperiod = int(search_dict['timeperiod'])
        indicator = search_dict['indicator'].lower().replace(" ", "")
        indicator_threshold = float(search_dict['threshold'])
        interval = search_dict['interval'].replace(" ", "").lower()

        symbols = moving_averages(indicator, interval, timeperiod, indicator_threshold, symbols)

    return symbols
