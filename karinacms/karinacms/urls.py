from django.conf.urls import patterns, include, url

from django.contrib import admin
from lead_center import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'lead_center.views.index', name='index'),
    # url(r'^blog/', includelead_center('blog.urls')),
     url(r'^leads/', include('lead_center.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

# if settings.DEBUG:
#         urlpatterns += patterns(
#                 'django.views.static',
#                 (r'media/(?P<path>.*)',
#                 'serve',
#                 {'document_root': settings.MEDIA_ROOT}), )
