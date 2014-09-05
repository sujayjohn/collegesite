from django.conf.urls import patterns, include, url
from rss import views

from rss.feeds import *

urlpatterns = patterns('',
    url(r'^$',views.home,name='news_home'),    
    url(r'^rss$',TEB(),name='news_rss'),
    url(r'^(?P<docid>\d+)',views.notice,name='notice'),
    url(r'^add$',views.add_new,name='notice_add_new'),
    url(r'^approve$',views.approve_notices,name='notices_approve'),
    )
