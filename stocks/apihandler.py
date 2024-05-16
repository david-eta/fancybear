"""

Note:
- Utilizes the requests library to make HTTP requests to the Alpha Vantage API.
- Utilizes regex and string manipulation to format dictionary keys.
- Utilizes the Decimal class to ensure accurate representation of decimal values.
- The 'get_chart_data' function reverses the order of the chart values dictionary to display the data in chronological order.
"""

import requests
from re import compile, sub
from decimal import Decimal, ROUND_HALF_UP
from datetime import date

#  ----------------------- HELPER FUNCTIONS ---------------------------
def adjust(val):
  # change the price strings to 2 decimal-place numbers
  return Decimal(val).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

def format_dic(dic: dict, date: str) -> dict:
  
  # renaming the keys
  d = compile(r'\d') # regex for any digit (0-9)
  # remove any digits, remove '. ', and replace any other spaces with underscores(_)
  dic = {sub(d, '', key.replace('. ', '').replace(' ', '_')).lower(): value for key, value in dic.items()}
  
  # reformatting decimal types
  try:
    if date == 'current':
      dic['open'] = adjust(dic['open'])
      dic['high'] = adjust(dic['high'])
      dic['low'] = adjust(dic['low'])
      dic['price'] = adjust(dic['price'])
      dic['previous_close'] = adjust(dic['previous_close'])
      dic['change'] = adjust(dic['change'])
    
    else:
      dic['open'] = adjust(dic['open'])
      dic['high'] = adjust(dic['high'])
      dic['low'] = adjust(dic['low'])
      dic['close'] = adjust(dic['close'])
      dic['adjusted_close'] = adjust(dic['adjusted_close'])
      dic['volume'] = adjust(dic['volume'])
      dic['dividend_amount'] = adjust(dic['dividend_amount'])
      dic['split_coefficient'] = adjust(dic['split_coefficient'])
     
  except KeyError:
    dic = None
  
  return dic
#  --------------------- HELPER FUNCTIONS END ------------------------


key = 'FW2H8DGS1C7FY99C'
#'stock_details': Fetches global quote details for a given stock ticker from the Alpha Vantage API and formats the response into a dictionary with adjusted decimal values.
def stock_details(ticker = 'AAPL'):
  url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol='+ticker+'&entitlement=delayed&apikey='+key
  r = requests.get(url)
  info = r.json()['Global Quote - DATA DELAYED BY 15 MINUTES']
  return format_dic(info, 'current')
#'search_results': Performs a symbol search based on keywords using the Alpha Vantage API and returns a list of tuples containing symbol and company name matches.
def search_results(search_input = 'BA'):
  url = 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords='+search_input+'&apikey='+key
  r = requests.get(url)
  res = []
  matches = r.json()['bestMatches']
  for match in matches:
    res.append((match['1. symbol'], match['2. name']))
  return res

#'historical_stock_price': Fetches historical stock price data for a given stock ticker and date from the Alpha Vantage API and formats the response into a dictionary with adjusted decimal values.
def historical_stock_price(ticker, date):
  try:
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol='+ticker+'&outputsize=full&apikey='+key
    r = requests.get(url)
    data = r.json()['Time Series (Daily)'][date]
    return format_dic(data, 'historical')
  except KeyError:
    return {'error': 'key'}

#- 'get_chart_data': Retrieves chart data for a given stock ticker and time interval from the Alpha Vantage API. The time interval can be 'month', 'week', or 'intraday', and the function returns a dictionary of date-value pairs for the closing prices.
def get_chart_data(ticker, timeInterval):
  url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol='+ticker+'&outputsize=full&apikey='+key
  chart_values = {}
  if timeInterval == 'month':
    r = requests.get(url)
    data = r.json()["Time Series (Daily)"]
    count = 0
    for date, value in data.items():
      if count < 30:
        chart_values[date] = value['4. close']
        count += 1
      else:
        break
  elif timeInterval == 'week':
    r = requests.get(url)
    data = r.json()["Time Series (Daily)"]
    count = 0
    for date, value in data.items():
      if count < 7:
        chart_values[date] = value['4. close']
        count += 1
      else:
        break
  else:
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='+ticker+'&interval=15min&entitlement=delayed&apikey='+key
    r = requests.get(url)
    data = r.json()
    for date, values in data["Time Series (15min)"].items():
      chart_values[date] = values["4. close"]
  ret =  dict(reversed(list(chart_values.items()))) # it's backwards. this reverses it
  return ret