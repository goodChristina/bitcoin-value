"""
Query Parameters for coinbase api
"""

import requests as r
import sys
from time import sleep

url = "https://api.coinbase.com/v2/exchange-rates?currency=BTC"

resp = r.get(url)


us_bitcoin = float(resp.json()["data"]["rates"]["USD"])
uk_bitcoin = float(resp.json()["data"]["rates"]["GBP"])

message = f"\nIf you had bitcoin, each one would be worth ${us_bitcoin:.2f}, or £{uk_bitcoin:.2f}.\n"


def type_bitcoin(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(delay)
    print()


type_bitcoin(message)
