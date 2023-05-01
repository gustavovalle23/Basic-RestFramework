from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)
    birth_date = models.DateField()
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["date_of_birth"]

    objects = UserManager()

    def __str__(self) -> str:
        return self.email
