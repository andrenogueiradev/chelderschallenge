from django.db.models.fields.related import ManyToManyField
from django.db import models
from .validators import validate_CNPJ, valida_cnpj

from accounts.models import Client


class Company(models.Model):
    clients = ManyToManyField(Client)
    company_name = models.CharField(max_length=30, blank=True, null=True)
    cnpj = models.CharField('CNPJ', max_length=18, validators=[validate_CNPJ, valida_cnpj], blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=90, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.company_name
