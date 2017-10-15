from django.conf.urls import url
from .views import post_detail, post_list, post_new

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', post_detail, name="detail"),
    url(r'^list/$', post_list, name="list"),
    url(r'^new/', post_new, name="new")
]