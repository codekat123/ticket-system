from django.contrib.auth.models import AbstractUser
from django.db import models
from .manager import CustomUserManager


class User(AbstractUser):
    username = None
    first_name = None
    last_name = None

    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=200)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.email
