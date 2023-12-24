from django.db import models
from django.contrib.auth. models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserAccountsManager():
    pass

class UserAccount(AbstractBaseUser, PermissionsMixin):
    """This model overides basic user save"""
    email = models.EmailField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountsManager()
