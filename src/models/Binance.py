import os
import time

import ccxt
import pandas as pd

class Binance:

    _api_key = os.getenv("BINANCE_API_KEY")
    _secret_key = os.getenv("BINANCE_API_SECRET")

    def __init__(self):
        self._exchange = ccxt.binance(
            {
                'apiKey': self._api_key,
                'secret': self._secret_key
            }
        )

    def load_data(self):
        print("Loading data from Binance")

    def account_balance(self):
        timestamp = int(time.time() * 1000)
        account_balance = self._exchange.fetch_balance(params={'timestamp': timestamp})
        return pd.DataFrame(account_balance['info']['balances'])
    
    def account_balance_more_than_zero(self):
        # Assign free and locked to numeric
        account_balance = self.account_balance()
        account_balance['free'] = pd.to_numeric(account_balance['free'])
        account_balance['locked'] = pd.to_numeric(account_balance['locked'])

        filtered_balance = account_balance[(account_balance['free'] > 0) | (account_balance['locked'] > 0)]
        return filtered_balance
    
    def to_csv(self, data, name="default.csv", path='data/'):
        data.to_csv(path + name)

class Spot(Binance):

    def __init__(self):
        super().__init__()

class Future(Binance):

    def __init__(self):
        self._exchange = ccxt.binance({
            'apiKey': self._api_key,
            'secret': self._secret_key,
            'options': {
                'defaultType': 'future'
            }
        })

    def account_balance(self):
        account_balance = self._exchange.fetch_balance()
        return pd.DataFrame(account_balance['info']['assets'])
    
    def account_balance_more_than_zero(self):
        # Assign walletBalance and marginBalance to numeric
        balance_futures = self.account_balance()
        balance_futures['walletBalance'] = pd.to_numeric(balance_futures['walletBalance'])
        balance_futures['marginBalance'] = pd.to_numeric(balance_futures['marginBalance'])

        filtered_balance_future = balance_futures[(balance_futures['walletBalance'] > 0) | (balance_futures['marginBalance'] > 0)]
        return filtered_balance_future