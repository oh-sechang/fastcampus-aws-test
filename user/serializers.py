from rest_framework import serializers
from user.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = ['id', 'shop_name', 'shop_address']
        fields = '__all__'

