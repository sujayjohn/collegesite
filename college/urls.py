from django.conf.urls import patterns, include, url
from college import views


urlpatterns = patterns('',
    url(r'^$',views.home,name='college_home'),
    url(r'^society/(?P<soc_name>\S+)?/?',views.society,name='society_home'),
    url(r'^department/(?P<dept_name>\S+)?/?',views.department,name='department_home'),
    url(r'^events',views.events,name='events_home'),
    url(r'^alumni/',views.alumni,name='alumni_home'),
    url(r'^contact$',views.contact_us,name='contact_us'),
    url(r'^principal',views.principal,name='principal_home'),
    url(r'^archive/',views.archive,name='archive_home'),
    url(r'^academics/',views.academics_home,name='academics_home'),
    url(r'^admissions/',views.admissions_home,name='admissions_home'),
    )
