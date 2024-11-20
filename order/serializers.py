from rest_framework import serializers
from order.models import Shop, Menu, Order 

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        #fields = ['id', 'shop_name', 'shop_address']
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'