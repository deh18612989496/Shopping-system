
from django.urls import path
from goods.views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('foodtype', FoodTypeView)
router.register('market', MarketView)
urlpatterns = [
    # 首页接口
    path('home/', home)
]
urlpatterns += router.urls
