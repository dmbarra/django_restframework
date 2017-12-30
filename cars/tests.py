# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from model_mommy import mommy
from cars.models import Car

class TestRecord(TestCase):

    def setUp(self):
        self.car = mommy.make(Car, name='Gol')

    def test_record_creation(self):
        self.assertTrue(isinstance(self.car, Car))
        self.assertEquals(self.car.__str__(), self.car.name)