from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.competitions_list),
    url(r'^competition/(?P<pk>[0-9]+)/$', views.competitions_signup, name='competitions_signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'^login/invalid/$', views.invalid_login, name='invalid_login'),
    url(r'^login/logged/$', views.logged, name='logged'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^registration/success$', views.reg_success, name='reg_success'),
]