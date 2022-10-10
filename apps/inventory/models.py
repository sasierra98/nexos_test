from django.db import models
from django.utils.translation import gettext_lazy as _

from base_model.models import BaseModelAbstract, User, Branch, Product


class Inventory(BaseModelAbstract):
    inventory_date = models.DateField(
        verbose_name=_('Inventory date')
    )

    gln_user = models.ForeignKey(
        to=User,
        verbose_name=_('GLN client'),
        on_delete=models.CASCADE
    )

    gln_branch = models.ForeignKey(
        to=Branch,
        verbose_name=_('GLN branch'),
        on_delete=models.CASCADE
    )

    gtin_product = models.ForeignKey(
        to=Product,
        verbose_name=_('Gtin product'),
        on_delete=models.CASCADE
    )

    quantity = models.IntegerField(
        verbose_name=_('Quantity')
    )
