# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AZIranianBankGatewaysConfig(AppConfig):
    name = "azbank"
    verbose_name = _("Iranian bank gateway")
    verbose_name_plural = _("Iranian bank gateways")
    # compatible with django >= 3.2
    default_auto_field = "django.db.models.AutoField"
