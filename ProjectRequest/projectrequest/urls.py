from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('projectrequest.views',
(r'^$', 'showIndex'),
(r'^thanks/$', 'showThanks'),
)