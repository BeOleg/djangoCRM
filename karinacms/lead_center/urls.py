from django.conf.urls import patterns, include, url

from django.contrib import admin
from lead_center import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'lead_center.views.index', name='index'),
    url(r'^about/', 'lead_center.views.about', name='about'),
    url(r'^form/(?P<campaign_name>.+)?', 'lead_center.views.lead_form', name='contact'),
    url(r'^lead-page/(?P<lead_name>.+)?', 'lead_center.views.lead_page', name='lead_page'),
    # url(r'^blog/', includelead_center('blog.urls')),
    url(r'^register/', 'lead_center.views.register', name='register'),
    url(r'^login/', 'lead_center.views.user_login', name='login'),
    url(r'^logout/', 'lead_center.views.user_logout', name='logout'),
    #url(r'^admin/', include(admin.site.urls)),
)