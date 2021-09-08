import os
from binance.client import Client

# init
api_key = os.environ.get('binance_test_key')
api_secret = os.environ.get('binance_test_secret')

print(api_key, api_secret)