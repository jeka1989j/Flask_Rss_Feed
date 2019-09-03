import requests
import json


def get_currency(from_curr, to_curr):
    key = 'e62f164167bc5f14d2c75fa1'
    currency_url = f'https://v3.exchangerate-api.com/bulk/{key}/USD'
    # data = requests.get(req_url).text
    # read_data = json.loads(data)
    # print(read_data)
    resp = requests.get(currency_url)
    read_data = resp.json()
    from_rate = read_data['rates'].get(from_curr.upper())
    to_rate = read_data['rates'].get(to_curr.upper())
    return (to_rate / from_rate, read_data['rates'].keys())
