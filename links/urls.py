from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'shortener.views.homepage', name='home'),
    url(r'^thanks/', 'shortener.views.thanks', name='thanks'),
    url(r'^top/', 'shortener.views.list_top_domain_monthly', name='top'),
    url(r'^last', 'shortener.views.list_last_hundred', name = 'last'),
    url(r'^admin/', include(admin.site.urls)),
)
