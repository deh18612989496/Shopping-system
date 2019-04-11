from django.core.cache import cache
from rest_framework.authentication import BaseAuthentication

from user.models import AXFUser
from utils.error import PramsException


class UserTokenAuthentication(BaseAuthentication,):
    # 认证
    def authenticate(self, request):
        try:
            #三元
            #token = request.query_params.get('token') if request.query_params.get('token') else request.data.get('token')
            #判断
            if request.query_params.get('token'):
                token = request.query_params.get('token')
            else:
                token = request.data.get('token')
            user_id = cache.get(token)
            user = AXFUser.objects.get(pk=user_id)
            return user, token
        except:
            raise PramsException({'code':1009, 'msg':'用户没登录'})