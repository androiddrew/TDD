from django.conf.urls import patterns, include, url
#patterns() returns a formated list to the urlpatternsfrom django.contrib import admin
#include is used to source a urls defined in an application specific urls.py file
#url ....
urlpatterns = patterns('',
	#patterns() returns a formated list to the urlpatterns
    # Examples:
    url(r'^$', 'list.views.home_page', name='home'),
    url(r'^lists/the-only-list-in-the-world/$', 'list.views.view_list', name='view_list'),
    url(r'^lists/new$', 'list.views.new_list', name= 'new_list'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^/', 'superlists.list.views', name = 'home_page')
)
