from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class User(AbstractUser):
    address = models.CharField(max_length=255, blank=True, null=True)

    objects = UserManager()
