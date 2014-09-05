from django.conf.urls import patterns, include, url
from docs import views
from django.contrib.auth.forms import AuthenticationForm

urlpatterns = patterns('',
    url(r'^$',views.home,name='docs_home'),
    url(r'^(?P<docid>\d+)',views.status,name='docs_status'),    
    url(r'^office/',views.office,name='docs_office'),
    url(r'^add$',views.add,name='docs_add'),
    url(r'^edit$',views.edit),
    url(r'^new/(?P<docid>\d+)',views.newly_added,name='docs_newly_added'),

)
