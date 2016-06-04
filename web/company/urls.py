from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    # url(r'^main/', views.main_list, name = 'main_list'),
    url(r'^main_list/(?P<companyid>\d+)/$', views.main_list, name = 'main_list'),
    url(r'^main_list/[0-9]/(?P<pk>[0-9]+)/$', views.main_detail, name = 'main_detail'),
    # url(r'^content_list/(?P<pk>[0-9]+/$', views.content_list, name = 'content_list')
]
