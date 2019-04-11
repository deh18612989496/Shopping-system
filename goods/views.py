import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from django_redis import get_redis_connection

from goods.filters import GoodsFilter
from goods.models import MainWheel, MainNav, MainMustBuy, MainShop, MainShow


# def home(request):
#     if request.method == 'GET':
#         return JsonResponse()
from goods.serializers import *


@api_view(['GET'])
def home(request):
    # TODO: 如何优化查询, 如何设置存储的格式（默认为bytes）, json
    # 如果使用redis缓存数据，类型: hash散列
    # hset key field value
    # hset goods main_wheels MainWheelSerializer(main_wheels, many=True).data
    # hset goods main_navs MainNavSerializer(main_navs, many=True).data
    conn = get_redis_connection()
    redis_main_wheels = conn.hget('goods', 'main_wheels')
    if not redis_main_wheels:
        main_wheels = MainWheel.objects.all()
        new_main_wheels = MainWheelsSerializer(main_wheels, many=True).data
        # 存储结果为json格式数据，json.dumps()
        value_wheels = json.dumps(new_main_wheels)
        conn.hset('goods', 'main_wheels', value_wheels)
    redis_main_wheels = conn.hget('goods', 'main_wheels')
    # 存储为字符串类型的结果值，需转换为字典，json.loads()
    old_main_wheels = json.loads(redis_main_wheels)

    # main_wheels = MainWheel.objects.all()
    main_navs = MainNav.objects.all()
    main_mustbuys = MainMustBuy.objects.all()
    main_shops = MainShop.objects.all()
    main_shows = MainShow.objects.all()

    res = {
        'main_wheels': old_main_wheels,
        'main_navs': MainNavsSerializer(main_navs, many=True).data,
        'main_mustbuys': MainMustBuySerializer(main_mustbuys, many=True).data,
        'main_shops': MainShopsSerializer(main_shops, many=True).data,
        'main_shows': MainShowsSerializer(main_shows, many=True).data
    }
    return Response(res)


class FoodTypeView(viewsets.GenericViewSet,
                   mixins.ListModelMixin):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer

class MarketView(viewsets.GenericViewSet,
                 mixins.ListModelMixin):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    filter_class = GoodsFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        #分类
        typeid = self.request.query_params.get('typeid')
        foodtype = FoodType.objects.filter(typeid=typeid).first()
        # 全部分类：

        a = foodtype.childtypenames.split('#')
        foodtypenames_list = [{'child_name': i.split(':')[0], 'child_value': i.split(':')[1]} for i in a]

        # foodtypenames = foodtype.childtypenames.split('#')
        # foodtypenames_list = []
        # for i in foodtypenames:
        #
        #     data = {
        #     'child_name':i.spalit(':')[0],
        #     'child_value':i.spalit(':')[1]
        #     }
        #     foodtypenames_list.append(data)
        rule_list = [
            {'order_name':'综合排序', 'order_value': 0},
            {'order_name':'综合升序', 'order_value': 1},
            {'order_name':'综合降序', 'order_value': 2},
            {'order_name':'销量升序', 'order_value': 3},
            {'order_name':'销量降序', 'order_value': 4},
        ]
        res = {
            'goods_list': serializer.data,
            'foodtype_childname_list': foodtypenames_list,#需要chile_name和child_value
            'order_rule_list': rule_list,
        }
        return Response(res)