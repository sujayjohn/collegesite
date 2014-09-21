from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^',include('college.urls')),
    url(r'^login/$','django.contrib.auth.views.login',{'template_name':'college/login.html'}),
    url(r'^logout/$','django.contrib.auth.views.logout',{'template_name':'college/logged_out.html'}),
    
    url(r'^news/',include('rss.urls')),
    url(r'^office/',include('docs.urls')),
    url(r'^roombook/',include('roombook.urls')),
    url(r'^attendence/',include('attendence.urls')),
    
    url(r'^webmaster/', include(admin.site.urls)),
)
