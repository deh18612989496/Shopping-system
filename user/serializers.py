import uuid

from django.contrib.auth.hashers import make_password, check_password
from rest_framework import serializers
from rest_framework.response import Response
from django.core.cache import cache

from user.models import AXFUser
from utils.error import PramsException


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AXFUser
        #序列化所有字段
        fields = '__all__'


class UserRegisterSerializer(serializers.Serializer):
    # 只是用于校验字段
    # 和前段人员沟通好需要校验字段的名称
    u_username = serializers.CharField(required=True,
                                       max_length=32,
                                       min_length=4,
                                       error_messages={
                                           'required':'注册账号必填',
                                           'max_length':'注册账号不能超过32位',
                                           'min_length': '注册账号不能短于4位',
                                       })
    u_password = serializers.CharField(required=True,
                                       max_length=10,
                                       min_length=3,
                                       error_messages={
                                           'required': '密码必填',
                                           'max_length': '密码不能超过10位',
                                           'min_length': '密码不能短于3位',
                                       })
    u_password2 = serializers.CharField(required=True,
                                        max_length=10,
                                        min_length=3,
                                        error_messages={
                                            'required': '确认密码必填',
                                            'max_length': '确认密码不能超过10位',
                                            'min_length': '确认密码不能短于3位',
                                        })
    u_email = serializers.CharField(required=True, )

    def validate(self, attrs):
        # 判断用户是否注册，
        username = attrs.get('u_username')
        if AXFUser.objects.filter(u_username=username).exists():
            raise PramsException({'code': 1001, 'msg':'注册账号已经存在'})
        # 判断密码是否一致，
        if attrs.get('u_password')!= attrs.get('u_password2'):
            raise PramsException({'code': 1002, 'msg':'密码不一致'})
        # 判断邮箱是否存在
        if AXFUser.objects.filter(u_email=attrs.get('u_email')).exists():
            raise PramsException({'code': 1003, 'msg':'邮箱已经存在'})
        return attrs

    def register_data(self, validata_data):
        #实现注册功能
        u_password = make_password(validata_data['u_password'])
        user = AXFUser.objects.create(u_username=validata_data['u_username'],
                               u_password=u_password,
                               u_email=validata_data['u_email'])

        res = {
            'code': 200,
            'msg': '注册成功',
            'user_id': user.id
        }
        return Response(res)

class UserLoginSerializer(serializers.Serializer):
    u_username = serializers.CharField(required=True,
                                       max_length=32,
                                       min_length=4,
                                       error_messages={
                                           'required': '注册账号必填',
                                           'max_length': '注册账号不能超过32位',
                                           'min_length': '注册账号不能短于4位',
                                       })
    u_password = serializers.CharField(required=True,
                                       max_length=10,
                                       min_length=3,
                                       error_messages={
                                           'required': '密码必填',
                                           'max_length': '密码不能超过10位',
                                           'min_length': '密码不能短于3位',
                                       })
    def validate(self, attrs):
        # 判断账号是否存在
        if not AXFUser.objects.filter(u_username=attrs.get('u_username')).exists():
            raise PramsException({'code':1005, 'msg':'账号不存在登录失败'})
        #判断密码是否正确
        user = AXFUser.objects.filter(u_username=attrs.get('u_username')).first()
        if not check_password(attrs.get('u_password'), user.u_password):
            raise PramsException({'code':1006, 'msg':'密码错误，登录失败'})
        return attrs

        #是否登录
    def login_date(self, validate_date):
        #登录
        token = uuid.uuid4().hex
        user = AXFUser.objects.filter(u_username = validate_date['u_username']).first()
        #cache使用redis进行存储
        #set存储的是字符串类型的值
        cache.set(token, user.id, timeout=60 * 60 * 7)
        res = {
            'token': token
        }
        return res