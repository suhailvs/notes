
from django.conf.urls import patterns, include, url
from userprofile.views import profileUpdate
urlpatterns = patterns('userprofile.views',
    url(r'^settings/$', 'profile',name='user_profile'),
    url(r'^uploadpic/$', 'uploadpic',name='upload_pic'),
    url(r'^update/$', profileUpdate.as_view(), name='profile_update'),  
    url(r'^login/$', 'social_login',name="auth_login"),  
)