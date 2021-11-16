from requirement_keys import *
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import datetime
from datetime import date, timedelta

def new_token_update():
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
  parameters = {
    'start':'1',
    'limit':'250',
    'convert':'USD'
  }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': key,
  }

  session = Session()
  session.headers.update(headers)

  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    # print(data)
    today = date.today()
    yesterday = str(today -timedelta(days=1))
    yesterday_datetime = datetime.datetime.strptime(yesterday,'%Y-%m-%d')

    for entry in data['data']:
      symbol = entry["symbol"]
      total_pairs = entry['num_market_pairs']
      c_supply = entry["circulating_supply"]
      total_supply = entry["total_supply"]
      max_supply = entry["max_supply"]
      tags = entry['tags']
      criteria = [symbol,total_supply,c_supply,total_pairs,max_supply,tags]
      # print(criteria)

      # print('SYMBOL: ' , symbol , '\nCIRCULATING SUPPLY: ' + c_supply +
      #       '\nTOTAL SUPPLY: ' + total_supply + '\nMAX SUPPLY: ' + max_supply +
      #       '\nTAGS: ' + tags)
      date_added_str = entry['date_added'][:10]
      date_added = datetime.datetime.strptime(date_added_str, '%Y-%m-%d')
      if yesterday_datetime < date_added:
        print(criteria)
      else:
        pass
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)


def exchange_volume():
  url = 'https://pro-api.coinmarketcap.com/v1/exchange/info'

  parameters = {
    'start': '1',
    'limit': '50',
    'convert': 'USD'
  }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': key,
  }
  session = Session()
  session.headers.update(headers)

  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    print(data)
    # for exchange in m:
    #   name = exchange['name']
    #   maker_fee = exchange['maker_fee']
    #   taker_fee = exchange['taker_fee']
    #   spot_vol = exchange["spot_volume_usd"]
    #   curr_fiats = exchange['fiats']
    #   useful =[name, spot_vol, curr_fiats, maker_fee, taker_fee]
    #   print(useful)
  except (ConnectionError,Timeout, TooManyRedirects) as e:
    print(e)



new_token_update()