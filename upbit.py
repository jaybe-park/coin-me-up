import requests
import json
import util_redis


upbit_urls = {
    'market': 'https://api.upbit.com/v1/market/all',
    'ticker': 'https://api.upbit.com/v1/ticker',
}

upbit_redis_key = {
    'market': 'upbit_market',
    'ticker': 'upbit_ticker',
}


def get_quotation_header():
    header = {"Accept": "application/json"}
    return header


def get_markets_from_api(isDetails=False):
    type = 'market'

    url = upbit_urls[type]
    header = get_quotation_header()
    params = {'isDetails': isDetails}

    response = requests.get(url, headers=header, params=params)
    data = json.loads(response.text)

    return data


def get_markets(isDetails=False):
    r = util_redis.get_redis_connection()
    key = upbit_redis_key['market']
    
    if not r.exists(key):
        markets = get_markets_from_api(isDetails=isDetails)
        markets = list(map(lambda x: x['market'], markets))

        r.rpush(key, *markets)
    else:
        markets = r.lrange(key, 0, -1)

    r.close()

    return markets


def get_ticker_from_api(markets):
    type = 'ticker'

    url = upbit_urls[type]
    header = get_quotation_header()
    params = {'markets': ','.join(markets)}

    response = requests.get(url, headers=header, params=params)
    data = json.loads(response.text)

    return data