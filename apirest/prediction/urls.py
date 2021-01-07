from django.conf.urls import url
from .views import intention_list, intention_detail, buy_or_not_buy

urlpatterns = [
    url(r'^shopper/$', intention_list),
    url(r'^shoppers/(?P<pk>[0-9]+)/$', intention_detail),
    url(r'^intention/$', buy_or_not_buy),
]