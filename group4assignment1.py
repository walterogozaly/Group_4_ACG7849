import requests
r = requests.get('https://api.coinmarketcap.com/data-api/v3/topsearch/rank')

# get top searches
top = r.json()["data"]["cryptoTopSearchRanks"]
top
