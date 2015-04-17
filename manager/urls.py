from django.conf.urls import patterns, url

from manager import views


urlpatterns = patterns('',

    url(r'^$', views.index,name='index'),

    url(r'^elements/list/$', views.elements_index,name='elements_index'),
    url(r'^elements/(?P<element_id>\d+)/$', views.element_details, name='element_details'),
    url(r'^elements/add/(?P<buylist_id>\d+)/$', views.element_add, name='element_add'),
    url(r'^elements/add/$', views.element_add, name='element_add'),
    url(r'^elements/del/(?P<element_id>\d+)/$', views.element_del, name='element_del'),
    url(r'^elements/chaneimg/(?P<element_id>\d+)/$', views.element_change_img, name='element_change_img'),



    url(r'^buylists/list/$', views.buylist_index,name='buylist_index'),
    url(r'^buylists/add/$', views.buylist_add,name='buylist_add'),
    url(r'^buylists/(?P<buylist_id>\d+)/$', views.buylist_details, name='buylist_details'),
    url(r'^buylists/delete/(?P<buylist_id>\d+)/$', views.buylist_delete, name='buylist_delete'),
    url(r'^buylist_add_elements/(?P<buylist_id>\d+)/$', views.buylist_add_elements, name='buylist_add_elements'),
    url(r'^buylist/elements/status/(?P<buylistelement_id>\d+)/$', views.buylist_element_status_ajax, name='buylist_element_status_ajax'),
    url(r'^buylist/elements/delete/(?P<buylistelement_id>\d+)/$', views.buylist_element_delete, name='buylist_element_delete'),
    url(r'^get_element_list_by_type/(?P<elementtype_id>\d+)/$', views.get_element_list_by_type, name='get_element_list_by_type'),
    url(r'^buylists/elements/comment/(?P<buylistelement_id>\d+)/$', views.buylist_element_get_comment, name='buylist_element_get_comment'),
    url(r'^buylists/elements/comment/add/(?P<buylistelement_id>\d+)/$', views.buylist_element_add_comment, name='buylist_element_add_comment'),

    url(r'^login/$', views.loginuser, name='loginuser'),
    url(r'^logout/$', views.logoutuser, name='logoutuser'),



)