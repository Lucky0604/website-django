from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', 'intro.views.intro_main', name = 'intro_main'),
]