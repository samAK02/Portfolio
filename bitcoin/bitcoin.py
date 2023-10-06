import sys
import json
import requests


def main():
    if len(sys.argv) == 2:
        try:
            value = float(sys.argv[1])
        except ValueError:
            print("Command-line argument is not a number")
            sys.exit(1)
    else:
        print("Missing command-line argument")
        sys.exit(1)
    try:
        r = requests.get(" https://api.coindesk.com/v1/bpi/currentprice.json")
        rate = r.json()
        price = rate["bpi"]["USD"]["rate_float"]
        amount = float(price) * float(sys.argv[1])
        print(f"${amount:,.4f}")

    except requests.RequestException:
        sys.exit()


main()
