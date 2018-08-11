from django.db import models

# Create your models here.
class Currency(models.Model):
    BLOCKCHAIN_CHOICES = (
        ('BTC', 'btc'),
        ('ETH', 'eth'),
        ('LTC', 'ltc'),
        ('OMNI', 'omni'),
    )
    """
        decimal_point(integer)
        is_base(boolean)
        reusable(boolean)
        address_length(integer)
    """
    icon = models.CharField(max_length=200)
    name = models.CharField(max_length=200, unique=True)
    ticker = models.CharField(max_length=5, primary_key=True)
    withdrawal_fee = models.DecimalField(max_digits=50, decimal_places=5, default=0)
    withdrawal_minimum = models.DecimalField(max_digits=50, decimal_places=5, default=0)
    blockchain_type = models.CharField(max_length=5, choices=BLOCKCHAIN_CHOICES, default='BTC')
    decimal_point = models.PositiveIntegerField(default=0)
    is_base = models.BooleanField(default=False)
    is_reusable = models.BooleanField(default=False)
    sync_deposit = models.BooleanField(default=False)
    ERC20 = models.BooleanField(default=False)
    abi = models.TextField(max_length=200, default="{}")
    transaction_confirmation_count = models.PositiveIntegerField(default=1)
    contract_address = models.CharField(max_length=200, default='')
    address_length = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.ticker


class Pair(models.Model):
    trade = models.ForeignKey(Currency, related_name='trade', on_delete=models.CASCADE)
    base = models.ForeignKey(Currency, related_name='base', on_delete=models.CASCADE, limit_choices_to={'is_base': True})
    trade_name = models.ForeignKey(Currency, related_name='trade_name', on_delete=models.CASCADE, default='',
                                   to_field='name')
    base_name = models.ForeignKey(Currency, related_name='base_name', on_delete=models.CASCADE,
                                  limit_choices_to={'is_base': True}, default='')
    transaction_fee = models.DecimalField(max_digits=50, decimal_places=5, default=0)
    decimal_point_trade = models.PositiveIntegerField(default=1)
    decimal_point_base = models.PositiveIntegerField(default=1)
    total_minimum = models.DecimalField(max_digits=50, decimal_places=5, default=0)
    tag = models.BooleanField(default=False)
    note = models.CharField(max_length=200, default='')
    req_note = models.CharField(max_length=200, default='')

    @property
    def trade_pair(self):
        return "%s-%s" % (self.trade, self.base)


    # def __str__(self):
    #     return str(self.trade)+"-"+str(self.base)