# coding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class Capoeirista(models.Model):
    GRADUATIONS = (
        (0, _('Mestre')),
        (1, _('Formado')),
        (2, _('Formado')),
        (3, _('Professor')),
        (4, _('Instrutor')),
    )

    BELTS = {
        0: '-',
        1: _('Preta'),
        2: _('Marrom'),
        3: _('Verde e Roxa'),
        4: _('Azul')
    }

    name = models.CharField(_(u'nome'), max_length=255)
    nickname = models.CharField(_(u'apelido'), max_length=50)
    phone = models.CharField(_(u'telefone'), max_length=30)
    email = models.EmailField(_(u'email'), blank=True)
    graduation = models.IntegerField(_(u'graduação'), max_length=3, choices=GRADUATIONS)
    user = models.OneToOneField(User)
    created_at = models.DateTimeField(_('criado em'), auto_now_add=True)

    class Meta:
        ordering = ['nickname']
        verbose_name = _('capoeirista')
        verbose_name_plural = _('capoeiristas')

    def __unicode__(self):
        return u'%s %s (%s)' % (self.GRADUATIONS[self.graduation][1], self.nickname, self.belt)

    @property
    def belt(self):
        return self.BELTS[self.graduation]


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


class Photo(models.Model):
    event = models.ForeignKey(Event)
    title = models.CharField(_(u'título'), max_length=100)
    description = models.TextField(_(u'descrição'), blank=True)
    photo = models.ImageField(upload_to='event_photos')
