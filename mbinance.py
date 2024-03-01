'''
!/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2023-04-09 17:11
@Author  : V2_Airdrops https://discord.gg/NB8BBMRqAj
'''
import time

import requests
from binance.spot import Spot


# https://binance-docs.github.io/apidocs/spot/cn/#1f6f90f1a7
# https://binance-connector.readthedocs.io/en/latest/
# pip install binance-connector
class Binacce:

    def __init__(self):
        self.client = Spot(api_key='Your Api Key',
                           api_secret='Your Api Secret')

    # 提币 其他可选参数见https://binance-connector.readthedocs.io/en/latest/binance.spot.wallet.html#withdraw-user-data
    def withdraw2(self, amount, toAds):
        data = {
            "coin": "ETH",
            "address": toAds,
            "amount": amount,
        }
        response = self.client.withdraw(**data)
        print(response)


Binacce().withdraw2("0.1", "0x...")
