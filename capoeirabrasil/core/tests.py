# coding: utf-8

from datetime import datetime
from datetime import date
from django.test import TestCase
from django.contrib.auth.models import User
from model_mommy import mommy
from capoeirabrasil.core.models import Capoeirista, Event


class EventModelTest(TestCase):
    def setUp(self):
        capoeirista = mommy.make(Capoeirista)

        self.obj = Event(
            title=u'Evento Chuleta',
            description='Evento de teste',
            date=date.today(),
            capoeirista=capoeirista
        )

    def test_create(self):
        """
        Event should have title, description, date ans capoeirista
        """
        self.obj.save()
        self.assertEqual(1, self.obj.pk)

    def test_has_created_at(self):
        """
        Event must have automatic created_at
        """
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        """
        Unicode returns the model name
        """
        self.assertEqual(self.obj.title, unicode(self.obj))


class CapoeiristaModelTest(TestCase):
    def setUp(self):
        user = mommy.make(User)

        self.obj = Capoeirista(
            name=u'José Conceição',
            phone='219999-9999',
            email='mestredoidao@capoeirabrasil.com.br',
            graduation='FP',
            user=user
        )

    def test_create(self):
        """
        Capoeirista should have name, phone, email, user and graduation
        """
        self.obj.save()
        self.assertEqual(1, self.obj.pk)

    def test_has_created_at(self):
        """
        Capoeirista must have automatic created_at
        """
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        """
        Unicode returns the model name
        """
        self.assertEqual(self.obj.name, unicode(self.obj))
