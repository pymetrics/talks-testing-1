# accounts/models/user.py
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

from .mixins import SlackAuthMixin
from .managers import SlackUserManager

class SlackUser(SlackAuthMixin, AbstractBaseUser):
    USERNAME_FIELD = 'user_id'
    user_id = models.CharField(max_length=50, primary_key=True)
    team_id = models.CharField(max_length=50)
    display_name = models.CharField(max_length=100)

    objects = SlackUserManager

    class Meta:
        unique_together = ('user_id', 'team_id')
