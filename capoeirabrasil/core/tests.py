# coding: utf-8

from django.test import TestCase
from capoeirabrasil.core.models import Capoeirista


class CapoeiristaModelTest(TestCase):
    # falta user e address
    def setUp(self):
        self.obj = Capoeirista(
            name='Nome',
            phone='219999-9999',
            email='mestredoidao@capoeirabrasil.com.br',
            graduation='FP'
        )

    def test_create(self):
        """
        Capoeirista should have name, phone, email and graduation
        """
        self.obj.save()
        self.assertEqual(1, self.obj.pk)
