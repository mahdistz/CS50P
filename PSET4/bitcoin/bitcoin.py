import requests
import sys
import re


def find_numbers(string):
    return re.findall(r"[-+]?(?:\d*\.*\d+)", string)

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    elif not find_numbers(sys.argv[1]):
        sys.exit("Command-line argument is not a number")
    else:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        if response.status_code == 200:
            amount = response.json().get("bpi").get("USD").get("rate")
            amount = float(amount.replace(",", "")) * float(sys.argv[1])
            print(f"${amount:,.4f}")
except requests.RequestException:
    pass


