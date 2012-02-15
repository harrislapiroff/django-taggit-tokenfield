from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
	url(r'^tags/', 'taggittokenfield.views.filter_tags'),
)