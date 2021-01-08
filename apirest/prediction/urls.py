from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^shoppers/$', shoppers_list),
    url(r'^shopper/(?P<pk>[0-9]+)/$', shopper_detail),
    url(r'^intention/$', buy_or_not_buy),
]