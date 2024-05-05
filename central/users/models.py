from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, Group, Permission


class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.

    Username and password are required. Other fields are optional.
    """

    groups = models.ManyToManyField(Group, related_name="user_groups")
    user_permissions = models.ManyToManyField(
        Permission, related_name="user_permissions"
    )
    objects = UserManager()

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
