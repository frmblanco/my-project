from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.competitions_list),
    url(r'^competition/(?P<pk>[0-9]+)/$', views.competitions_signup, name='competitions_signup'),
]