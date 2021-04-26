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


url = "https://finviz.com/quote.ashx?t="

full_url = url + "aapl"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/68.0.3440.106 Safari/537.36', }
response = requests.get(full_url, headers=headers).content

soup = bs4.BeautifulSoup(response, 'html.parser')

average_volume = soup.find("td", text="Price").find_next_sibling("td").text

print(average_volume)

print(str_value_to_num(average_volume)



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
this = ['A', 'AA', 'AAL', 'AAPL', 'ABBV', 'ABC', 'ABT', 'ACAD', 'ACB', 'ACGL', 'ACI', 'ACN', 'ADBE', 'ADI', 'ADM', 'ADP', 'ADT', 'ADVM', 'AEE', 'AEM', 'AEO', 'AEP', 'AES', 'AFL', 'AFMD', 'AG', 'AGI', 'AGIO', 'AHCO', 'AI', 'AIG', 'AKAM', 'ALE', 'ALK', 'ALKS', 'ALL', 'ALLY', 'ALXN', 'AM', 'AMAT', 'AMC', 'AMCR', 'AMD', 'AME', 'AMGN', 'AMRS', 'AMTX', 'AMWL', 'AMZN', 'ANF', 'ANGI', 'AON', 'APA', 'APD', 'APH', 'APHA', 'APPS', 'APTV', 'AQN', 'AQUA', 'AR', 'ARCO', 'ARDX', 'ARLO', 'ARMK', 'ARRY', 'ARVL', 'ASAN', 'ASB', 'ASO', 'ATEN', 'ATH', 'ATUS', 'ATVI', 'AUPH', 'AVA', 'AVGO', 'AVTR', 'AVXL', 'AVYA', 'AWK', 'AXP', 'AXTA', 'AY', 'BA', 'BAC', 'BAH', 'BAM', 'BAX', 'BB', 'BBBY', 'BBY', 'BCE', 'BCRX', 'BDX', 'BE', 'BEN', 'BG', 'BGCP', 'BHC', 'BIIB', 'BK', 'BKR', 'BLDP', 'BLDR', 'BLL', 'BLNK', 'BLUE', 'BMY', 'BNGO', 'BNL', 'BNS', 'BOX', 'BRKS', 'BSX', 'BTBT', 'BTG', 'BWA', 'BYD', 'BYND', 'BZH', 'C', 'CADE', 'CAG', 'CAH', 'CARR', 'CAT', 'CB', 'CBRE', 'CC', 'CCJ', 'CCK', 'CCL', 'CDE', 'CDNS', 'CENX', 'CERN', 'CERS', 'CF', 'CFG', 'CGC', 'CHKP', 'CHNG', 'CHPT', 'CHRS', 'CHRW', 'CHTR', 'CHWY', 'CI', 'CIEN', 'CL', 'CLDR', 'CLF', 'CLNE', 'CLR', 'CLSK', 'CLVS', 'CMA', 'CMCSA', 'CME', 'CMI', 'CMS', 'CNC', 'CNHI', 'CNK', 'CNP', 'CNQ', 'CNR', 'CNX', 'COF', 'COG', 'COMM', 'COP', 'COST', 'COTY', 'CPB', 'CPE', 'CPRI', 'CPRT', 'CREE', 'CRIS', 'CRM', 'CRON', 'CRSP', 'CRWD', 'CSCO', 'CSIQ', 'CSX', 'CTSH', 'CTVA', 'CVA', 'CVAC', 'CVE', 'CVS', 'CVX', 'CYH', 'CZR', 'D', 'DAL', 'DB', 'DBX', 'DCT', 'DD', 'DDD', 'DDOG', 'DE', 'DELL', 'DFS', 'DG', 'DGX', 'DHI', 'DHR', 'DHT', 'DIS', 'DISCA', 'DISH', 'DKNG', 'DKS', 'DLTR', 'DMTK', 'DNB', 'DOCU', 'DOW', 'DRI', 'DT', 'DUK', 'DVA', 'DVAX', 'DVN', 'DXC', 'EA', 'EAF', 'EBAY', 'ED', 'EDIT', 'EGO', 'EIX', 'EL', 'ELAN', 'ELY', 'EMR', 'ENB', 'ENDP', 'ENPH', 'EOG', 'EPZM', 'EQH', 'EQT', 'EQX', 'ERF', 'ES', 'ESI', 'ESNT', 'ETN', 'ETR', 'ETRN', 'ETSY', 'EURN', 'EVRG', 'EW', 'EXC', 'EXEL', 'EXK', 'EXPD', 'EXPE', 'EXPI', 'EXTR', 'F', 'FANG', 'FAST', 'FB', 'FBP', 'FCEL', 'FCX', 'FDX', 'FE', 'FEYE', 'FGEN', 'FHN', 'FIS', 'FISV', 'FITB', 'FIZZ', 'FL', 'FLEX', 'FLIR', 'FLR', 'FNB', 'FND', 'FOLD', 'FOXA', 'FRO', 'FSLR', 'FSLY', 'FSM', 'FSR', 'FTCH', 'FTI', 'FTNT', 'FTOC', 'FTV', 'FUBO', 'G', 'GAN', 'GBX', 'GD', 'GDRX', 'GE', 'GES', 'GEVO', 'GFL', 'GILD', 'GIS', 'GLNG', 'GLUU', 'GLW', 'GM', 'GME', 'GNMK', 'GNTX', 'GO', 'GOGO', 'GOLD', 'GOOG', 'GOOGL', 'GPK', 'GPRE', 'GPRO', 'GPS', 'GRBK', 'GRMN', 'GRUB', 'GRWG', 'GS', 'GSAH', 'GT', 'HAL', 'HAS', 'HBAN', 'HBI', 'HBM', 'HCA', 'HD', 'HE', 'HES', 'HEXO', 'HFC', 'HGV', 'HIG', 'HL', 'HLT', 'HMHC', 'HOG', 'HOLX', 'HOME', 'HON', 'HPE', 'HPQ', 'HRB', 'HRL', 'HRTX', 'HSY', 'HTGC', 'HUM', 'HWM', 'HYLN', 'HZNP', 'IAA', 'IBM', 'ICE', 'ICPT', 'IDA', 'IEX', 'IFF', 'IGT', 'IIVI', 'ILMN', 'IMAX', 'INFO', 'INO', 'INSG', 'INTC', 'IONS', 'IOVA', 'IP', 'IPG', 'IPHI', 'IQV', 'IR', 'IRWD', 'ISBC', 'ITW', 'IVZ', 'JBHT', 'JBLU', 'JCI', 'JEF', 'JNJ', 'JNPR', 'JPM', 'JWN', 'K', 'KAR', 'KBH', 'KBR', 'KDP', 'KEY', 'KEYS', 'KGC', 'KHC', 'KL', 'KMB', 'KMI', 'KNX', 'KO', 'KODK', 'KOPN', 'KPTI', 'KR', 'KSS', 'KSU', 'KTOS', 'LAC', 'LB', 'LBTYK', 'LC', 'LDOS', 'LEN', 'LESL', 'LEVI', 'LHX', 'LIN', 'LITE', 'LKQ', 'LLY', 'LMND', 'LMNX', 'LMT', 'LNC', 'LNT', 'LOW', 'LPX', 'LRCX', 'LSCC', 'LTHM', 'LTRPA', 'LUMN', 'LUV', 'LVS', 'LW', 'LYB', 'LYFT', 'LYV', 'M', 'MA', 'MAR', 'MARA', 'MAS', 'MAT', 'MAXN', 'MAXR', 'MCD', 'MCFE', 'MCHP', 'MCO', 'MDLZ', 'MDT', 'MET', 'MFC', 'MGI', 'MGM', 'MGNI', 'MITK', 'MMC', 'MMM', 'MNST', 'MO', 'MOS', 'MP', 'MPC', 'MPLN', 'MRK', 'MRNA', 'MRO', 'MRVL', 'MS', 'MSFT', 'MT', 'MTB', 'MTCH', 'MTDR', 'MTG', 'MU', 'MUR', 'MVIS', 'MWK', 'MXIM', 'NAVI', 'NCLH', 'NCR', 'NDAQ', 'NEE', 'NEM', 'NET', 'NFLX', 'NI', 'NIO', 'NKE', 'NKLA', 'NKTR', 'NLOK', 'NLS', 'NLSN', 'NNOX', 'NOC', 'NOV', 'NOVA', 'NRG', 'NSC', 'NTAP', 'NTNX', 'NTR', 'NTRA', 'NTRS', 'NUAN', 'NUE', 'NVAX', 'NVCR', 'NVDA', 'NVST', 'NVTA', 'NWG', 'NWL', 'NWSA', 'NXPI', 'NYCB', 'NYT', 'OCGN', 'OKE', 'OKTA', 'OLLI', 'OLN', 'OMC', 'ON', 'ORA', 'ORBC', 'ORCC', 'ORCL', 'ORI', 'OSH', 'OSTK', 'OTIS', 'OVV', 'OXY', 'PAAS', 'PACB', 'PAGS', 'PAYA', 'PAYX', 'PBCT', 'PBF', 'PBI', 'PCAR', 'PCG', 'PCRX', 'PEG', 'PENN', 'PEP', 'PERI', 'PFE', 'PFG', 'PFGC', 'PG', 'PGEN', 'PGNY', 'PGR', 'PHM', 'PING', 'PINS', 'PLAN', 'PLTR', 'PLUG', 'PM', 'PNC', 'PNR', 'PPD', 'PPG', 'PPL', 'PRSP', 'PRTY', 'PRU', 'PRVB', 'PSEC', 'PSN', 'PSTG', 'PSTH', 'PSX', 'PTC', 'PTON', 'PXD', 'PYPL', 'QCOM', 'QRTEA', 'QSR', 'RAD', 'RCL', 'RDFN', 'RDWR', 'REAL', 'REGI', 'REGN', 'RF', 'RFP', 'RIDE', 'RIOT', 'RKT', 'RLGY', 'ROKU', 'ROOT', 'ROST', 'RP', 'RRC', 'RSG', 'RTX', 'RUN', 'RXT', 'RY', 'SABR', 'SAND', 'SAVA', 'SAVE', 'SBLK', 'SBUX', 'SCHW', 'SDC', 'SEAS', 'SEDG', 'SEE', 'SFIX', 'SFM', 'SGEN', 'SGMS', 'SHW', 'SI', 'SIRI', 'SITC', 'SJI', 'SKX', 'SLB', 'SLM', 'SM', 'SNAP', 'SNOW', 'SO', 'SONO', 'SPCE', 'SPGI', 'SPLK', 'SPNE', 'SPR', 'SPWR', 'SQ', 'SRE', 'SRNE', 'SSRM', 'SSYS', 'STE', 'STL', 'STLD', 'STM', 'STNE', 'STPK', 'STT', 'STX', 'STZ', 'SU', 'SUMO', 'SVM', 'SWI', 'SWK', 'SWKS', 'SYF', 'SYNH', 'SYY', 'T', 'TAP', 'TBIO', 'TCBI', 'TD', 'TDOC', 'TECK', 'TEL', 'TER', 'TFC', 'TGNA', 'TGT', 'TGTX', 'TJX', 'TLRY', 'TMHC', 'TMO', 'TMUS', 'TOL', 'TPH', 'TPIC', 'TPR', 'TPX', 'TRGP', 'TRIP', 'TRMB', 'TROW', 'TRP', 'TRQ', 'TRU', 'TRV', 'TSCO', 'TSLA', 'TSN', 'TTC', 'TTCF', 'TTWO', 'TU', 'TWLO', 'TWNK', 'TWTR', 'TXN', 'U', 'UA', 'UAA', 'UAL', 'UBER', 'UBS', 'UFS', 'UMPQ', 'UNH', 'UNM', 'UNP', 'UPS', 'UPWK', 'URBN', 'USB', 'USFD', 'UUUU', 'V', 'VCYT', 'VERU', 'VET', 'VFC', 'VFF', 'VG', 'VIAC', 'VIVO', 'VLDR', 'VLO', 'VLY', 'VMW', 'VRNT', 'VRT', 'VRTX', 'VST', 'VTRS', 'VUZI', 'VXRT', 'VZ', 'W', 'WAB', 'WAL', 'WBA', 'WDAY', 'WDC', 'WEC', 'WEN', 'WFC', 'WIFI', 'WKHS', 'WM', 'WMB', 'WMT', 'WORK', 'WPM', 'WPRT', 'WRK', 'WSC', 'WSM', 'WTRG', 'WU', 'WW', 'WYNN', 'X', 'XEL', 'XLNX', 'XOM', 'XPO', 'XRAY', 'XRX', 'YETI', 'YUM', 'Z', 'ZI', 'ZION', 'ZM', 'ZNGA', 'ZS', 'ZTS']
print(len(this))