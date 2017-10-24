from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.competitions_list),
    url(r'^competition/(?P<pk>[0-9]+)/$', views.competitions_signup, name='competitions_signup'),
    url(r'^competition/(?P<pk>[0-9]+)/success/$', views.comp_success, name='comp_success'),
]