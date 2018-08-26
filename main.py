# -*- coding: utf-8 -*-

import requests
from pprint import pprint

URL = 'https://neoscan.io'
BLOCK = 2640000
NEO = 'c56f33fc6ecfcd0c225c4ab356fee59390af8560be0e930faebe74a6daff7c9b'
BALANCE = 'api/main_net/v1/get_balance'
ABSTRACTS = 'api/main_net/v1/get_address_abstracts'


def get(address):

    url_balance = "/".join([URL, BALANCE, address])
    url_abstracts = "/".join([URL, ABSTRACTS, address, "1"])

    items = requests.get(url_balance).json()
    # pprint(items)
    for item in items['balance']:
        if item.get('asset') == "NEO":
            balance = item['amount']

    items = requests.get(url_abstracts).json()
    # pprint(items)

    for item in items['entries']:
        if item.get('block_height') > BLOCK and item.get('asset') == NEO:
            # print(item['address_to'], float(item.get('amount')))
            # pprint(item)
            if item['address_to'] == address:
                balance -= float(item.get('amount'))
            else:
                balance += float(item.get('amount'))
    return balance


def main():

    add_a='AXDt2hzT35knLnV3MB3dR9rAvYmadUfVdb'
    add_b='AKnbvRwL1MSPFWoS6bdD5v2SNHq2uta5tm'
    
    print(f"Answer: {get(add_a)}")
    print(f"Answer: {get(add_b)}")

if __name__ == '__main__':
    main()


