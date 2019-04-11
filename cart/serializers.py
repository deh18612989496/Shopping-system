
from rest_framework import serializers

from cart.models import Cart
from goods.serializers import GoodsSerializer


class CartSerializer(serializers.ModelSerializer):
    c_goods = GoodsSerializer()
    class Meta:
        model = Cart
        fields = '__all__'
