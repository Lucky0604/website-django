from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^company/', views.company_list, name = 'company_list'),
    url(r'^post/', views.post_list, name = 'post_list'),
]
