from django.db import models
from django.utils.translation import gettext_lazy as _

from base_model.models import BaseModelAbstract


class Product(BaseModelAbstract):
    gtin_product = models.PositiveIntegerField(
        verbose_name=_('Gtin product'),
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

    unit_value = models.FloatField(
        verbose_name=_('Unit value')
    )
