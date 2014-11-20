from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'hrmanager.views.login', name='login'),
    url(r'^employee/', include('employee.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hradmin/', include("hradmin.urls")),


)
