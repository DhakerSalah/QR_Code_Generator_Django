from django.shortcuts import render
from rest_framework import viewsets

from myApp.models import Item
from myApp.serializer import ItemSerializer
# Create your views here.

class Items(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer