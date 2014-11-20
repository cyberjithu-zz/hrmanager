from django.conf.urls import patterns, url
from hradmin import views

urlpatterns = patterns('/',
                       url(r'^/hradmin/$', views.index, name='index'),
                       # url(r'')
                       )
