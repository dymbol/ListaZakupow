from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',
	# Examples:
	#url(r'^$', 'ListaZakupow.views.home', name='home'),
	# url(r'^ListaZakupow/', include('ListaZakupow.foo.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	# url(r'^admin/', include(admin.site.urls)),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^manager/', include('manager.urls')),
	url(r'^$', include('manager.urls')),
	#url(r'^$', 'index'),
	#url(r'^elements/(?<Element_id>\d+)/$, 'elements_view'),

	#(r'^(?P<poll_id>\d+)/$', 'detail'),
	#(r'^(?P<poll_id>\d+)/results/$', 'results'),
	#(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)
