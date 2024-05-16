import requests

key = 'FW2H8DGS1C7FY99C'
url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey='+key
r = requests.get(url)
data = r.json()

# print(data)


# for search 

#url = 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=BA&apikey='+key
#r = requests.get(url)
#matches = r.json()['bestMatches']

# print(matches)

#for match in matches:
#  print(match['1. symbol'] + ' ' + match['2. name'])

def historical_stock_price(ticker, date):
  url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ticker+'&outputsize=full&apikey='+key
  r = requests.get(url)
  data = r.json()['Time Series (Daily)'][date]
  return data

print(historical_stock_price('AAPL','2024-03-28'))


