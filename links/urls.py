from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'shortener.views.homepage', name='home'),
    url(r'^thanks/', 'shortener.views.thanks', name='thanks'),
    url(r'^top/', 'shortener.views.list_hundred_popular', name='top'),
    url(r'^admin/', include(admin.site.urls)),
)
