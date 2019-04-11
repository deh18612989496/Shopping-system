from django.shortcuts import render
from rest_framework import viewsets, mixins
from django.core.cache import cache

# Create your views here.
from rest_framework.decorators import list_route
from rest_framework.response import Response

from user.models import AXFUser
from user.serializers import UserSerializer, UserRegisterSerializer, UserLoginSerializer
from utils.error import PramsException


class UserView(viewsets.GenericViewSet,
               mixins.RetrieveModelMixin,
               mixins.ListModelMixin,
               ):
    #用户相关数据
    queryset = AXFUser.objects.all()
    #序列化
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        token = request.query_params.get('token')
        user_id = cache.get(token)
        user = AXFUser.objects.filter(id=user_id).first()
        serializer = self.get_serializer(user)
        #TODO: 订单数量的筛选
        res = {
            'user_info':serializer.data
        }
        return Response(res)

    @list_route(methods=['POST'], serializer_class=UserRegisterSerializer)
    def register(self, request):
        # /api/user/user/register/  POST
        # 校验参数
        serializers = self.get_serializer(data=request.data)
        #如果校验失败， 直接往外抛出异常
        serializers.is_valid(raise_exception=False)
        if not request:
            raise PramsException({'code':1004, 'msg': '参数有误'})
        # 注册功能
        data = serializers.register_data(serializers.data)
        return data

    @list_route(methods=['POST'], serializer_class=UserLoginSerializer)
    def login(self, request):
        serializers = self.get_serializer(data=request.data)
        result = serializers.is_valid(raise_exception=False)
        if not result:
            raise PramsException({'code':1007, 'msg':'参数出错'})
        #登录功能
        res = serializers.login_date(serializers.data)
        return Response(res)
