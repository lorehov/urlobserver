# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url
from urlobserver.core import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='core-index'),
    url(r'^subscription_add/$', views.subscription_add),
)
