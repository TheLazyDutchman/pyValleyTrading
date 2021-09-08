import os
from binance import ThreadedWebsocketManager

import pprint
pp = pprint.PrettyPrinter(indent=4)


# init
api_key = os.environ.get('binance_test_key')
api_secret = os.environ.get('binance_test_secret')

btc_price = {'error':False}

def btc_trade_history(msg):
    ''' define how to process incoming WebSocket messages '''
    if msg['e'] != 'error':
        pp.pprint(msg['c'])
        btc_price['last'] = msg['c']
        btc_price['bid'] = msg['b']
        btc_price['last'] = msg['a']
        btc_price['error'] = False
        pp.pprint(btc_price)
    else:
        btc_price['error'] = True


# init and start the WebSocket
socket = ThreadedWebsocketManager(api_key, api_secret, testnet = True)
socket.start()

# subscribe to a stream
stream = socket.start_symbol_ticker_socket(callback = btc_trade_history, symbol = 'BTCUSDT')

socket.join()