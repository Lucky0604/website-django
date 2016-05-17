from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    # url(r'^main/', views.main_list, name = 'main_list'),
    url(r'^main_list/$', views.main_list, name = 'main_list'),
]
