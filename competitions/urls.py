from django.conf.urls import include, url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.competitions_list),
    url(r'^competition/(?P<pk>[0-9]+)/$', views.competitions_signup, name='competitions_signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^registration/success$', views.reg_success, name='reg_success'),
]