from django.urls import path, re_path

from goodsIssue.views import issue, delGoods, saleHis, message

urlpatterns = [
        re_path(r'^issue', issue),
        re_path(r'^delGoods', delGoods),
        re_path(r'^saleHis', saleHis),
        re_path(r'message', message),
]