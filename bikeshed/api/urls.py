# coding=utf-8
from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^api/bike/add', views.add, name='api_add'),
    url(r'^api/bikes-sorted/(?P<sort>(model|brand|price)\b)/(?P<order>(asc|desc)\b)$', views.list_sorted, name='api_list_sorted'),
    url(r'^api/bikes', views.list, name='api_list'),
]
