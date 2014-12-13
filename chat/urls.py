from django.conf.urls import patterns, url
from chat import views

urlpatterns = patterns('/',
                       url(r'^$', views.index, name='index'),
                       url(r'^user-(?P<username>\w+)$', views.chatselect, name='chatselect'),
                       # url(r'^ajaxmessage/$', views.loadmessages, name='loadmessages')
                       )
