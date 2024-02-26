import requests
from re import compile, sub
from decimal import Decimal, ROUND_HALF_UP

#  ----------------------- HELPER FUNCTIONS ---------------------------
def adjust(val):
  # change the price strings to 2 decimal-place numbers
  return Decimal(val).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

def format_dic(dic: dict) -> dict:
  
  # renaming the keys
  d = compile(r'\d') # regex for any digit (0-9)
  # remove any digits, remove '. ', and replace any other spaces with underscores(_)
  dic = {sub(d, '', key.replace('. ', '').replace(' ', '_')).lower(): value for key, value in dic.items()}
  
  # reformatting decimal types
  dic['open'] = adjust(dic['open'])
  dic['high'] = adjust(dic['high'])
  dic['low'] = adjust(dic['low'])
  dic['price'] = adjust(dic['price'])
  dic['previous_close'] = adjust(dic['previous_close'])
  dic['change'] = adjust(dic['change'])
  
  return dic
#  --------------------- HELPER FUNCTIONS END ------------------------


key = 'FW2H8DGS1C7FY99C'

def stock_details(ticker):
  url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol='+ticker+'&apikey='+key
  r = requests.get(url)
  info = r.json()['Global Quote']
  return format_dic(info)

def search_results(search_input):
  url = 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords='+search_input+'&apikey='+key
  r = requests.get(url)
  res = []
  matches = r.json()['bestMatches']
  for match in matches:
    res.append((match['1. symbol'], match['2. name']))
  return res
