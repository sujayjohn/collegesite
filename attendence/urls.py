from django.conf.urls import patterns, include, url
from attendence import views
from django.contrib.auth.forms import AuthenticationForm

urlpatterns = patterns('',
    url(r'^(?P<classid>\S+)?$',views.home,name='attend_home'),

)
