from django.shortcuts import render
import json
from django.http import JsonResponse
from .models import Pair
from .models import Currency


# Create your views here.
def pair_detail(request):
    all_pairs = Pair.objects.all()
    pairs_info = Pair.objects.values('trade', 'base', 'trade_name', 'base_name', 'transaction_fee',
                                'decimal_point_trade', 'decimal_point_base', 'total_minimum', 'tag', 'note',
                                'req_note')  # or simply .values() to get all fields

    currency_info = Currency.objects.values('name', 'icon', 'ticker',
                                           'withdrawal_minimum',
                                           'decimal_point', 'is_base', 'is_reusable', 'address_length')

    currency = Currency.objects.values('ticker')
    currency_data = list()
    for c in currency:
        currency_data.append(c["ticker"])
    currency_list = currency_data

    data = list()
    for p in all_pairs:
        data.append(p.trade_pair)
    pairs = data
    pair_list = list(pairs_info)  # important: convert the QuerySet to a list object

    currencyInfoList = dict()
    currencyDict = dict()
    for info in currency_info:
        row = dict()
        row['name'] = info['name']
        row['icon'] = info['icon']
        row['withdrawal_minimum'] = info['withdrawal_minimum']
        row['decimal_point'] = info['decimal_point']
        row['is_base'] = info['is_base']
        row['is_reusable'] = info['is_reusable']
        row['address_length'] = info['address_length']
        currencyInfoList[info['ticker']] = row
        #append(currencyDict)

    pairInfoList = dict()
    pairDict = dict()
    for info in pairs_info:
        row = dict()
        row['base'] = info['base']
        row['trade'] = info['trade']
        row['base_name'] = info['base_name']
        row['trade_name'] = info['trade_name']
        row['transaction_fee'] = info['transaction_fee']
        row['decimal_point_trade'] = info['decimal_point_trade']
        row['decimal_point_base'] = info['decimal_point_base']
        row['total_minimum'] = info['total_minimum']
        row['tag'] = info['tag']
        row['note'] = info['note']
        row['req_note'] = info['req_note']
        pairInfoList[info['trade']+'-'+info['base']] = row
    #list(currency_info)
    #currencyDict['Ticker'] = list(currency_info)
    response = {
        "currency": currency_list, "pairs": pairs, "PairInfo": pairInfoList, "CurrencyInfo": currencyInfoList
    }
    return JsonResponse(response, safe=False)


"""

"ETH-BTC": {
            "base":"BTC",
            "trade":"ETH",
            "base_name": "Bitcoin",
            "trade_name":"Etherium",
            "transaction_fee":"0.00005",
            "trade_minimum":"0.50000",
            "base_minimum":"0.10000",
            "tag":false,
            "note":"This is a note.",
            "req_note":"This is a requirement note."
        }
        {
    "currency": ["BTC","ETH","LTC"],
    "pair" : ["ETH-BTC","LTC-BTC"],
    "currencyInfo":
    {
        "BTC": {
            "name":"Bitcoin",
            "icon":"https://www.cryptocompare.com/media/19633/btc.png?width=200",
            "withdrawl_minimum":"0.05000",
            "decimal_point":6,
            "is_base":true,
            "is_reusable":true,
            "address_length":40
        },
        "ETH":{
            "name":"Ethereum",
            "icon":"https://www.cryptocompare.com/media/19633/btc.png?width=200",
            "withdrawl_minimum":"0.05000",
            "decimal_point":6,
            "is_base":true,
            "is_reusable":true,
            "address_length":40
        },
       "LTC": {
            "name":"Litecoin",
            "icon":"https://www.cryptocompare.com/media/19633/btc.png?width=200",
            "withdrawl_minimum":"4.50000",
            "decimal_point":1,
            "is_base":false,
            "is_reusable":true,
            "address_length":40
        }
    },

    "pairInfo":{
        "ETH-BTC": {
            "base":"BTC",
            "trade":"ETH",
            "base_name": "Bitcoin",
            "trade_name":"Etherium",
            "transaction_fee":"0.00005",
            "trade_minimum":"0.50000",
            "base_minimum":"0.10000",
            "tag":false,
            "note":"This is a note.",
            "req_note":"This is a requirement note."
        },
        "LTC-BTC": {
            "base":"BTC",
            "trade":"LTC",
            "base_name": "Bitcoin",
            "trade_name":"Litecoin",
            "transaction_fee":"0.00000",
            "trade_minimum":"0.00000",
            "base_minimum":"0.00000",
            "tag":true,"note":"This is a note.",
            "req_note":"This is a requirement note."
        }
    }
}

"""