from statistics import mode
from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('id','url','name','qr_code')