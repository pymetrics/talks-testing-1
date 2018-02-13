# accounts/tests/test_account_creation.py
from django.test import TestCase
from django.contrib.auth.models import User
from accounts.models import CoinAccount

class CoinAccountCreationTests(TestCase):
    def test_account_defaults(self):
        test_user = User.objects.create(username='testuser')
        account = CoinAccount.objects.create(user=test_user)
        self.assertEqual(account.balance, 0.0)
