"""
Query Parameters for coinbase api
"""

import requests as r

url = "https://api.coinbase.com/v2/exchange-rates?currency=BTC"

resp = r.get(url)


us_bitcoin = float(resp.json()["data"]["rates"]["USD"])
uk_bitcoin = float(resp.json()["data"]["rates"]["GBP"])

print(
    f"\nIf you had bitcoin, each one would be worth ${us_bitcoin:.2f}, or £{uk_bitcoin:.2f}.\n"
)
