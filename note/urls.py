from django.conf.urls import patterns, include, url

urlpatterns = patterns('note.views',
    #plese check whar is addnote//
    
    url(r'^addnote/(new|\d+)/$', 'addnote',name='add_note'),
    url(r'^deletenote/$', 'delnote',name='delete_note'),   
    url(r'^publicnote/$', 'public',name='public_home'),
    url(r'^note/(\d+)/', 'publicnote',name='public_note'),
    url(r'^users/$', 'userlist',name='user_list'),
    url(r'^user/(\d+)/$', 'usernotes',name='user_notes'),    
    url(r'^tags/$', 'taglist', name='tags'),
    url(r'^addfolder/$', 'addfolder', name='add_folder'), 
)