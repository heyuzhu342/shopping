from django.urls import path, re_path

from trade.views import goodsList, goodsDetail, buyHis

urlpatterns = [
        re_path(r'^goodsList', goodsList),
        re_path(r'^goodsDetail', goodsDetail),
        re_path(r'^buyHis', buyHis),
]