import requests
import json
from config import keys, headers

class MoneyException(Exception):
    pass

class MoneyConverter:
    @staticmethod
    def convert(base: str, quote: str, amount: str):


        if quote == base:
            raise MoneyException(f'Невозможно перевести одинаковые валюты в {quote}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise MoneyException(f'Не удалось обработать валюту {quote}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise MoneyException(f'Не удалось обработать валюту {base}.')

        try:
            amount = float(amount)
        except ValueError:
            raise MoneyException(f'Не удалось обработать количество {amount}.')

        r = requests.request("GET", f'https://api.apilayer.com/fixer/convert?to={base_ticker}&from={quote_ticker}&amount={amount}', headers=headers)
        total_base = json.loads(r.content)["result"]

        return total_base
