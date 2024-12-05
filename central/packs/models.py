from django.db import models
from django.utils.translation import gettext_lazy as _
from app import settings
from users.models import User


class Package(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Package Name"))
    description = models.TextField(
        verbose_name=_("Package Description"), blank=True, null=True
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Price")
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Creation Date")
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Update Date"))
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="created_packages",
        verbose_name=_("Created By"),
    )

    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="updated_packages",
        verbose_name=_("Updated By"),
    )

    def __str__(self):
        return self.name


class UserPackage(models.Model):
    package = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="user_package",
        verbose_name=_("User Package"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="package_user",
        verbose_name=_("Package User"),
    )
    duration = models.DurationField(verbose_name=_("Signature Duration"))
    is_active = models.BooleanField(default=True, verbose_name=_("Package Status"))

    def __str__(self):
        return self.name
