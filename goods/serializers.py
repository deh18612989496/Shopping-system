
from rest_framework import serializers

from goods.models import *


class MainWheelsSerializer(serializers.ModelSerializer):
    class Meta:
        #序列化模型
        model = MainWheel
        #序列化字段
        fields = '__all__'


class MainNavsSerializer(serializers.ModelSerializer):
    class Meta:
        #序列化模型
        model = MainNav
        #序列化字段
        fields = '__all__'


class MainMustBuySerializer(serializers.ModelSerializer):
    class Meta:
        #序列化模型
        model = MainMustBuy
        #序列化字段
        fields = '__all__'


class MainShopsSerializer(serializers.ModelSerializer):
    class Meta:
        #序列化模型
        model = MainShop
        #序列化字段
        fields = '__all__'


class MainShowsSerializer(serializers.ModelSerializer):
    class Meta:
        #序列化模型
        model = MainShow
        #序列化字段
        fields = '__all__'


class FoodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodType
        fields = '__all__'


class GoodsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goods
        fields = '__all__'
