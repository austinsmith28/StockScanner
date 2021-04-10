import requests
import bs4

api_key = 'ddca75d268744b19b3cb78676aab6c54'
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
'''


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


url = "https://finviz.com/quote.ashx?t="

full_url = url + "aapl"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/68.0.3440.106 Safari/537.36', }
response = requests.get(full_url, headers=headers).content

soup = bs4.BeautifulSoup(response, 'html.parser')

average_volume = soup.find("td", text="Price").find_next_sibling("td").text

print(average_volume)

print(str_value_to_num(average_volume))
