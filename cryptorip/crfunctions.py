#!/usr/bin/env python3


from coinbase.wallet.client import Client
from credentials import *

client = Client(api_key, api_secret, api_version='2019-11-27')

# The currency code can be switched to EUR, CAD, JPY, etc.
currency_code = 'USD'


def btcprice():
    """Displays the current price of Bitcoin."""
    bitcoin = client.get_spot_price(currency_pair = 'BTC-USD')
    btc_message = f'The current price of Bitcoin is {bitcoin.amount} {currency_code}'
    print(btc_message)


def ltcprice():
    """Displays the current price of Litecoin."""
    litecoin = client.get_spot_price(currency_pair = 'LTC-USD')
    ltc_message = f'The current price of Litecoin is {litecoin.amount} {currency_code}'
    print(ltc_message)


def ethprice():
    """Displays the current price of Bitcoin."""
    ethereum = client.get_spot_price(currency_pair = 'ETH-USD')
    eth_message = f'The current price of Ethereum is {ethereum.amount} {currency_code}'
    print(eth_message)

if __name__ == '__main__':
    btcprice()
    ltcprice()
    ethprice()

