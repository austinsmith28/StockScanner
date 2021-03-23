# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import requests
import pandas as pd
api_key = 'ddca75d268744b19b3cb78676aab6c54'

ticker = 'MSFT'
interval = '1min'
technical = 'time_series'

api_url = f'https://api.twelvedata.com/{technical}?symbol={ticker}&interval={interval}&outputsize=12&apikey={api_key}'
data = requests.get(api_url).json()
pdData = pd.DataFrame(data['values'])

print(pdData)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
