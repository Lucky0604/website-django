from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^intro/$', views.intro, name = 'intro'),
]