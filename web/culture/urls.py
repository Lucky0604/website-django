from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<cultureid>\d+)/$', 'culture.views.culture_list', name = 'culture_list'),
]
