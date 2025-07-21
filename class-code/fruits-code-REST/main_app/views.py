from django.shortcuts import render, redirect
from .models import Fruit
from rest_framework import viewsets
from .serializers import FruitSerializer


class FruitViewSet(viewsets.ModelViewSet):
      queryset = Fruit.objects.all()
      serializer_class = FruitSerializer