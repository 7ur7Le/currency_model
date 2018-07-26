from django.contrib import admin
from currency.models import Currency, Pair

class PairTrade(admin.TabularInline):
    save_on_top = True
    model = Pair
    fk_name = 'trade'
    fields = ['base', 'trade_minimum', 'base_minimum']
    readonly_fields = ['trade']


class PairBase(admin.TabularInline):
    save_on_top = True
    model = Pair
    fk_name = 'base'
    fields = ['trade', 'trade_minimum', 'base_minimum']
    readonly_fields = ['base']



@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):

    #list_display = ('icon', 'name', 'ticker', 'blockchain_type')
    inlines = [PairTrade, PairBase]


@admin.register(Pair)
class CurrencyAdmin(admin.ModelAdmin):
    pass
    #list_display = ('icon', 'name', 'ticker', 'blockchain_type')
