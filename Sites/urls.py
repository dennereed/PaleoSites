from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Sites.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # app urls
    url(r'^$', 'paleosites.views.home', name='home'),
    url(r'^paleosites/', include('paleosites.urls', namespace="paleosites")),

    #admin urls
    url(r'^admin/', include(admin.site.urls)),

    # url(r'^$', 'paleosites.views.home', name='home'),
    # # e.g. /index/
    # url(r'^index', 'paleosites.views.home', name='home'),
    # # e.g. /kml/
    # url(r'^kml/', 'paleosites.views.all_kml', name='all_kml'),
    # # e.g. /map/
    # url(r'^map/', 'paleosites.views.map_page', name='map_page'),
)
