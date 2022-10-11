from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class User(AbstractUser, PermissionsMixin):
    gln_user = models.PositiveBigIntegerField(
        verbose_name=_('GLN client'),
        unique=True,
        primary_key=True
    )

    phone = models.CharField(
        verbose_name=_('Phone'),
        max_length=50,
        blank=True,
        null=True
    )

    address = models.CharField(
        verbose_name=_('Address'),
        max_length=255,
        blank=True,
        null=True
    )

