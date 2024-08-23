from django.urls import path,re_path
from goods import views


urlpatterns = [
    #查询所有商品
    path('goods/', views.goodsview.as_view(), name='goodsview'),
    #查询一个商品
    re_path('goods/(?P<pk>\d+)', views.goodsdetalview.as_view(), name='goodsdetalview'),
]
