from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


class BaseModelAbstract(models.Model):
    created_at = models.DateTimeField(
        verbose_name=_('Created at'),
        default=now
    )

    updated_at = models.DateTimeField(
        verbose_name=_('Created at'),
        default=now
    )

    class Meta:
        abstract = True
