
import django_filters

from goods.models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):

    typeid = django_filters.CharFilter('categoryid')
    childcid = django_filters.CharFilter('childcid', method='filter_childcid')
    order_rule = django_filters.CharFilter(method='filter_rule')

    class Meta:
        model = Goods
        fields = ['categoryid', 'childcid']

    def filter_rule(self, queryset, name, value):
        if value == '0':
            return queryset#自己定义的规则在哪里怎么点不进去
        elif value == '1':
            return queryset.order_by('price')
        elif value == '2':
            return queryset.order_by('-price')
        elif value == '3':
            return queryset.order_by('productnum')
        else:
            return queryset.order_by('-productnum')

    def filter_childcid(self, queryset, name, value):
        # 过滤方法
        if value == '0':
            return queryset
        else:
            return queryset.filter(childcid=value)



