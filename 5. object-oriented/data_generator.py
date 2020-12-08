import os
import time
import requests


def fetch_prices(api_key):
    res = requests.get(f"http://api.coinlayer.com/api/live?"
                       f"access_key={api_key}&target=EUR")
    rates = res.json()['rates']

    return {
        'bitcoin': rates['BTC'],
        'cardano': rates['ADA'],
        'ethereum': rates['ETH'],
        'iota': rates['MIOTA'],
        'tether': rates['USDT']
    }


def append_to_file(prices, file_path):
    serialized = (f"{prices['bitcoin']:.3f},{prices['cardano']:.3f},"
                  f"{prices['ethereum']:.3f},{prices['iota']:.3f},"
                  f"{prices['tether']:.3f}")

    with open(file_path, 'a') as f:
        f.write('\n' + serialized)


def main():
    api_key = os.environ['API_KEY']

    while True:

        print('Writting prices...')
        prices = fetch_prices(api_key)
        append_to_file(prices, 'cryptos.csv')
        time.sleep(30)


if __name__ == "__main__":
    main()
