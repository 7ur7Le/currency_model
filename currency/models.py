from django.db import models

# Create your models here.
class Currency(models.Model):
    BLOCKCHAIN_CHOICES = (
        ('BTC', 'btc'),
        ('ETH', 'eth'),
        ('LTC', 'ltc'),
    )
    """
        decimal_point(integer)
        is_base(boolean)
        reusable(boolean)
        address_length(integer)
    """
    icon = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
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
        return self.name


class Pair(models.Model):
    trade = models.ForeignKey(Currency, related_name='trade', on_delete=models.CASCADE)
    base = models.ForeignKey(Currency, related_name='base', on_delete=models.CASCADE, limit_choices_to={'is_base': True})
    transaction_fee = models.DecimalField(max_digits=50, decimal_places=5, default=0)
    trade_minimum = models.DecimalField(max_digits=50, decimal_places=5, default=0)
    base_minimum = models.DecimalField(max_digits=50, decimal_places=5, default=0)
    tag = models.BooleanField(default=False)
    note = models.CharField(max_length=200, default='')
    req_note = models.CharField(max_length=200, default='')

    def __str__(self):
        return str(self.trade)+"/"+str(self.base)