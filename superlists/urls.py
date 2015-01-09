from django.conf.urls import patterns, include, url
#patterns() returns a formated list to the urlpatternsfrom django.contrib import admin
#include is used to source a urls defined in an application specific urls.py file
#url ....
urlpatterns = patterns('',
	#patterns() returns a formated list to the urlpatterns
    # Examples:
    url(r'^$', 'list.views.home_page', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^/', 'superlists.list.views', name = 'home_page')
)
