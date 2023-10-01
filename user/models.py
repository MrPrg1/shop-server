from django.db import models

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager as BUM
from django.contrib.auth.models import PermissionsMixin
from rest_framework.serializers import ModelSerializer
from core.models import BaseModel

class BaseUserManager(BUM):
    def create_user(self, full_name, username, phone_number, address, is_active=True, is_admin=False, password=None, *args, **kwargs):

        if not phone_number:
            raise ValueError("Users must have an uniqe phone_number")

        user = self.model(
            full_name=full_name,
            username=username,
            phone_number=phone_number,
            address=address,
            is_active=is_active,
            is_admin=is_admin,
        )

        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.full_clean()
        user.save(using=self._db)
        return user

    def create_superuser(self, full_name, username, phone_number, address, password=None, *args, **kwargs):
        user = self.create_user(
            full_name=full_name,
            username=username,
            phone_number=phone_number,
            address=address,
            is_active=True,
            is_real_estate=False,
            is_admin=True,
            password=password,
        )

        user.is_superuser = True
        user.save(using=self._db)
        return user

class BaseUser(BaseModel, AbstractBaseUser, PermissionsMixin):
    
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    phone_number = models.IntegerField(unique=True)
    address = models.CharField(max_length=500)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = BaseUserManager()

    USERNAME_FIELD = "username"

    REQUIRED_FIELDS = ['full_name', "phone_number", 'address']

    def __str__(self):
        return f"{self.username} , {self.full_name}"

    def is_staff(self):
        return self.is_admin






# #serializers
# class UsersSerializer(ModelSerializer):

#     class Meta:
#         model = BaseUser
#         fields = ['id', 'full_name', 'username', 'phone_number', 'nationalـid', 'education', 'dateـofـbirth', 'userـtype']

