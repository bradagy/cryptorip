#!/usr/bin/env python3


import argparse


from crfunctions import btcprice
from crfunctions import ltcprice
from crfunctions import ethprice


parser = argparse.ArgumentParser()
parser.add_argument('--btc', dest='btcprice', help='Displays the current price of Bitcoin.',default=False,
                    action='store_true')
parser.add_argument('--ltc', dest='ltcprice', help='Displays the current price of Litecoin.', default=False,
                    action='store_true')
parser.add_argument('--eth', dest='ethprice', help='Displays the current price of Ethereum.', default=False,
                    action='store_true')
args = parser.parse_args()

if args.btcprice:
    btcprice()
elif args.ltcprice:
    ltcprice()
elif args.ethprice:
    ethprice()
