from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from notes.views import MyHome

urlpatterns = patterns('',
    url(r'^$', MyHome.as_view(), name='home'),    
    url(r'^doc/$', TemplateView.as_view(template_name="graphics.html"),name='documentation'),  
    url(r'^admin/', include(admin.site.urls)),
    url(r'^notes/', include('note.urls')),
    url(r'^profile/', include('userprofile.urls')),
    url(r'^logout/$', 'django.contrib.auth.views.logout',name="auth_logout"),
)

urlpatterns += patterns('notes.views',   
    url(r'^accounts/profile/$',MyHome.as_view(), name="profile"),
    url(r'^\+(.{5,500})$','url_note'),
    url(r'^ext/$','ext_note'),
    url(r'^ajx/$','ajx',name="ajax_load_to_div"),
    url(r'^deletefolder/$','deletefolder',name="delete_folder"), 
)


# site map stuffs
from note.sitemap import NoteSitemap
sitemaps = {
    'static': NoteSitemap,
}

urlpatterns += patterns('',
 url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
 )
