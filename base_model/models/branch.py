from django.db import models
from django.utils.translation import gettext_lazy as _


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

    is_active = models.BooleanField(
        verbose_name=_('active'),
        default=True
    )

