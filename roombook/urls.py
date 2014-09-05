from django.conf.urls import patterns, include, url
from roombook import views


urlpatterns = patterns('',
    url(r'^$',views.home,name='roombook_home'),
    url(r'^book$',views.add_new,name='room_booking'),
    url(r'^approve$',views.approve_reservations,name='roombook_approve'),
    )
