from django.conf.urls import patterns, include, url

from django.contrib import admin
from lead_center import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'lead_center.views.index', name='index'),
    # url(r'^about/', 'lead_center.views.about', name='about'),
    url(r'^add_lead/(?P<campaign_name>.+)?', 'lead_center.views.lead_form', name='add_lead'),
    url(r'^edit_lead/(?P<lead_id>\d+)/$', 'lead_center.views.lead_edit_form', name='edit_lead'),
    url(r'^lead_page/(?P<lead_name>.+)?', 'lead_center.views.lead_page', name='lead_page'),
    url(r'^products/', 'lead_center.views.product_list', name='product_list'),
    url(r'^campaigns/', 'lead_center.views.campaign_list', name='campaign_list'),
    url(r'^statuses/', 'lead_center.views.status_list', name='status_list'),
    # url(r'^blog/', includelead_center('blog.urls')),
    url(r'^register/', 'lead_center.views.register', name='register'),#TODO: remove those paths to the root urls.py
    url(r'^login/', 'lead_center.views.user_login', name='login'),
    url(r'^logout/', 'lead_center.views.user_logout', name='logout'),
    url(r'^search_list/$', 'lead_center.views.search_list', name='search_list'),
    url(r'^edit/(?P<obj_type>.+)/(?P<obj_id>\d+)$', 'lead_center.views.edit_obj', name='edit_obj'),   #url(r'^admin/', include(admin.site.urls)),
    url(r'^delete/(?P<obj_type>.+)/(?P<obj_id>\d+)$', 'lead_center.views.delete_obj', name='delete_obj'),
)