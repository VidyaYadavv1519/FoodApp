from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    item_image = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Item
        fields = ['id','item_name','item_desc','item_price','item_image']