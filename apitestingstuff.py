import requests

key = 'FW2H8DGS1C7FY99C'
url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey='+key
r = requests.get(url)
data = r.json()

# print(data)


# for search 

url = 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=BA&apikey='+key
r = requests.get(url)
matches = r.json()['bestMatches']

# print(matches)

for match in matches:
  print(match['1. symbol'] + ' ' + match['2. name'])