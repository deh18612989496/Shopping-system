
from django.urls import path
from rest_framework.routers import SimpleRouter
from cart.views import *


router = SimpleRouter()
router.register('cart', CartView)

urlpatterns = [

]
urlpatterns+=router.urls