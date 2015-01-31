# coding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Capoeirista(models.Model):
    GRADUATIONS = (
        ('ME', _('Mestre')),
        ('FP', _('Formado (Preta)')),
        ('FM', _('Formado (Marrom)')),
        ('PVR', _('Professor (Verde e Roxa)')),
        ('IA', _('Instrutor (Azul)')),
    )

    name = models.CharField(_(u'nome'), max_length=255)
    phone = models.CharField(_(u'telefone'), max_length=30)
    email = models.EmailField(_(u'email'), blank=True)
    graduation = models.CharField(_(u'graduação'), max_length=3, choices=GRADUATIONS)




