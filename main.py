import os
from binance.client import Client

import pprint
pp = pprint.PrettyPrinter(indent=4)



# init
api_key = os.environ.get('binance_test_key')
api_secret = os.environ.get('binance_test_secret')

client = Client(api_key, api_secret, testnet = True)


# get balances for all assets & some account information
pp.pprint(client.get_symbol_ticker(symbol = "BTCUSDT"))