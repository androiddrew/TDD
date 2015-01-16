from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^(\d+)/$', 'list.views.view_list', name='view_list'),
    url(r'^(\d+)/add_item$', 'list.views.add_item', name='add_item'),
    url(r'^new$', 'list.views.new_list', name='new_list'),
)