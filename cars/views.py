# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from cars.serializers import CarSerializer
from cars.models import Car

class CarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer