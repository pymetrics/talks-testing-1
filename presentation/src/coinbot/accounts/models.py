# accounts/models.py
from django.db import models
from coinbase import get_price

class CoinAccount(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    coin = models.CharField(max_length=3, default="BTC")
    balance = models.FloatField(default=0)

    def get_balance_in_fiat(self, fiat='USD'):
        """Account balance defaults to zero"""
        current_price = get_price(self.coin, fiat)
        return self.balance * current_price
