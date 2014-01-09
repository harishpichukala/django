from django.conf.urls  import *
urlpatterns=patterns('',
	(r'^$','myproject.apps.homepage.views.index'),
	)
