from django.conf.urls import patterns, include, url
from lead_center import views
from rest_framework import routers
from django.contrib import admin

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'leads_api', views.LeadViewSet)

urlpatterns = patterns('',
	url(r'^leads/', include('lead_center.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),

)

# if settings.DEBUG:
#         urlpatterns += patterns(
#                 'django.views.static',
#                 (r'media/(?P<path>.*)',
#                 'serve',
#                 {'document_root': settings.MEDIA_ROOT}), )
