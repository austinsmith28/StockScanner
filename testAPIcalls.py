import requests
from bs4 import BeautifulSoup, SoupStrainer

api_key = 'ddca75d268744b19b3cb78676aab6c54'


session = requests.Session()
adapter = requests.adapters.HTTPAdapter(
    pool_connections=100,
    pool_maxsize=100)
session.mount('https://', adapter)

'''
price_url = f'https://api.twelvedata.com/price?symbol=AAPL&apikey={api_key}'

stock_price = requests.get(price_url).json()

print(stock_price['price'])'''

'''
allStocksUrl = f'https://api.twelvedata.com/stocks'

allStockData = requests.get(allStocksUrl).json()

allSymbols = []

for i in allStockData['data']:
    print(i['symbol'], " is on ", i['exchange'], " in the ", i['country'])
'''

'''
url = "https://finance.yahoo.com/quote/"

full_url = url + "aapl"

response = requests.get(full_url).content

soup = bs4.BeautifulSoup(response, 'html.parser')


price = soup.body.find('span', class_="C($primaryColor) Fz(24px) Fw(b)").text

print(type(price))

#float_stock_price = float(stock_price)



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






url = f"https://api.twelvedata.com/ema?symbol=aapl&interval=1day&time_period=200&apikey={api_key}"


indicator_request = requests.get(url).json()
indicator_price = indicator_request['values'][0]['ema']

print(indicator_price)


url = f"https://api.twelvedata.com/ema?symbol=abcl&interval=1day&time_period=200&apikey={api_key}"
indicator_request = requests.get(url).json()

price_url = f'https://api.twelvedata.com/price?symbol=abcl&apikey={api_key}'
stock_price_request = requests.get(price_url).json()
try:
    stock_price = float(stock_price_request['price'])
    indicator_price = float(indicator_request['values'][0]['ema'])

    threshold = 20 * .01

    lower_threshold = stock_price * (1 - threshold)
    upper_threshold = stock_price * (1 + threshold)

    if lower_threshold <= indicator_price <= upper_threshold:
        print('yup')
except KeyError:
    print('value')



url = "https://finviz.com/quote.ashx?t="
counter =0
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/68.0.3440.106 Safari/537.36', }


full_url = url + "ping"

response = session.get(full_url, headers=headers).content
strainer = SoupStrainer('table', class_="snapshot-table2")
soup = BeautifulSoup(response, 'lxml', parse_only=strainer)


market_cap = soup.find("td", text="Market Cap").find_next_sibling("td").text

print(market_cap)

'''
url = "https://finviz.com/quote.ashx?t="

full_url = url + "aapl"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/68.0.3440.106 Safari/537.36', }
response = requests.get(full_url, headers=headers).content

soup = BeautifulSoup(response, 'html.parser')

average_volume = soup.find("td", text="Price").find_next_sibling("td").text

print(average_volume)

