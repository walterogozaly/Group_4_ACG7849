from selenium import webdriver
import time # needed for time.sleep
import requests
r = requests.get('https://api.coinmarketcap.com/data-api/v3/topsearch/rank')

# get top searches
top = r.json()["data"]["cryptoTopSearchRanks"]
top

print (top[0])

for i, t in enumerate(top):
    print("{}: {} ({}) ".format(i+1, t['name'], t['symbol']))

coin = top[0]

# new driver (opens browser window)
driver = webdriver.Chrome(executable_path='/Users/walterogozaly/Documents/chromedriver')

driver.get("https://www.reddit.com/")
theElement = driver.find_element_by_xpath(r'//*[@id="card_rank"]/section[2]/div[2]/div[1]/div[1]/span')
print(s)
print(s.text)

