"""
Query parameters for coinbase api, for bitcoin
C.Rin, April 2024
"""

import requests as r
import sys
from time import sleep
import datetime

# ANSI escape code
PURPLE = "\033[1;35m"
GREEN = "\033[1;32m"
NC = "\033[0m"

# coinbase api
url = "https://api.coinbase.com/v2/exchange-rates?currency=BTC"

resp = r.get(url)
current_time = datetime.datetime.now()

us_bitcoin = float(resp.json()["data"]["rates"]["USD"])
uk_bitcoin = float(resp.json()["data"]["rates"]["GBP"])

message = f"{GREEN}If you had bitcoin, each one would be worth ${us_bitcoin:.2f}, or £{uk_bitcoin:.2f}.{NC}\n"
border = f"{PURPLE}{'-'*70}{NC}\n"
time = f"Exact time is: {current_time}"


# typewriter
def typewriter(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(delay)


typewriter(border, delay=0.01)
print()
typewriter(message)
print(time, "\n")
typewriter(border, delay=0.01)
print()
