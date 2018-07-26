from django.shortcuts import render
import json
from django.http import JsonResponse
from .models import Pair
from .models import Currency


# Create your views here.
def pair_detail(request):
    # import pdb; pdb.set_trace()
    pairs = Pair.objects.values('trade', 'base', 'transaction_fee', 'trade_minimum', 'base_minimum', 'tag', 'note',
                                'req_note')  # or simply .values() to get all fields
    currency = Currency.objects.values('name', 'icon', 'ticker', 'blockchain_type', 'withdrawl_minimum', 'withdrawl_fee',
                                       'decimal_point', 'is_base', 'is_reusable', 'address_length', 'sync_deposit',
                                       'abi', 'ERC20', 'contract_address', 'transaction_confirmation_count')
    pair_list = list(pairs)  # important: convert the QuerySet to a list object
    currency_list = list(currency)
    response = {
        "currency": currency_list, "pair": pair_list
    }
    return JsonResponse(response, safe=False)

