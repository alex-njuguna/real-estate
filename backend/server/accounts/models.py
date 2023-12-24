from django.db import models
from django.contrib.auth. models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserAccountManager(BaseUserManager):
    """functionality to create a normal user and admin user"""
    def create_user(self, email, name, password=None):
        """create a normal user"""
        if not email:
            raise ValueError("A user must have an email!")
        
        email = self.normalize_email(email)

        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, email, name, password):
        """create a super user"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save()

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    """This model overides basic user save"""
    email = models.EmailField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()
