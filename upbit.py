import requests


upbit_urls = {
    'ticker': 'https://api.upbit.com/v1/ticker',
    'market': 'https://api.upbit.com/v1/market/all'
}


def get_quotation_header():
    header = {"Accept": "application/json"}
    return header


def get_ticker(markets):
    type = 'ticker'

    url = upbit_urls[type]
    header = get_quotation_header()
    params = {'markets': ','.join(markets)}

    requests.get(url, params=params)
