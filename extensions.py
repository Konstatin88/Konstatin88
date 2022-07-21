import requests
import json


currency = {
    'доллар': 'USD',
    'евро': 'EUR',
    'рубль': 'RUB',
    }


class ApiException(Exception):
    pass


class Converter:
    @staticmethod
    def get_price(base, quote, amount):
        try:
            base_key = currency[base.lower()]
        except KeyError:
            raise ApiException(f'Валюта {base} не найдена!')
        try:
            quote_key = currency[quote.lower()]
        except KeyError as e:
            raise ApiException(f'Валюта {quote} не найдена!')

        if base_key == quote_key:
            raise ApiException('Одинаковые валюты!')

        try:
            amount = float(amount.replace(',', '.'))
        except ValueError:
            raise ApiException(f'Не удалось обработать количество {amount}')

        r = requests.get(
            f'https://min-api.cryptocompare.com/data/price?fsym={base_key}&tsyms={quote_key}')
        resp = json.loads(r.content)
        ans = resp[quote_key] * float(amount)
        return round(ans, 2)
