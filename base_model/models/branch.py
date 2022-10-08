from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class Branch(models.Model):
    gln_branch = models.PositiveIntegerField(
        verbose_name=_('GLN branch'),
        primary_key=True,
        unique=True
    )

    name = models.CharField(
        verbose_name=_('Name'),
        max_length=50
    )

