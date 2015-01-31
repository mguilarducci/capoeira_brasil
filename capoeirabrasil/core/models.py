# coding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


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
    user = models.ForeignKey(User, null=True)
    created_at = models.DateTimeField(_('criado em'), auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name = _('capoeirista')
        verbose_name_plural = _('capoeiristas')

    def __unicode__(self):
        return u'%s' % self.name


class Event(models.Model):

    title = models.CharField(_(u'título'), max_length=100)
    description = models.TextField(_(u'descrição'))
    date = models.DateTimeField(_(u'data'))
    capoeirista = models.ForeignKey(Capoeirista)
    created_at = models.DateTimeField(_('criado em'), auto_now_add=True)

    class Meta:
        ordering = ['-date']
        verbose_name = _('evento')
        verbose_name_plural = _('eventos')

    def __unicode__(self):
        return u'%s' % self.title
