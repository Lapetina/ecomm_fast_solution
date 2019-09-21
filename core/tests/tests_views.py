# coding=utf-8

from __future__ import absolute_import, unicode_literals
from django.test import TestCase, Client
from django.urls import reverse
import unittest

from core import views

class indexViewTestCase(TestCase):

    #função para iniciar o teste
    def setUp(self):
        self.client = Client()
        self.url = reverse('index')

    #função para finalizar o teste
    def tearDown(self):
        pass

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_templeta_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'index.html')

if __name__ == '__main__':
    unittest.main()
