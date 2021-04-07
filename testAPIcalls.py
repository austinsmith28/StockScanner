import requests


api_key = 'ddca75d268744b19b3cb78676aab6c54'

price_url = f'https://api.twelvedata.com/price?symbol=AAPL&apikey={api_key}'

stock_price = requests.get(price_url).json()

print(stock_price['price'])