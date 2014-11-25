from django.conf.urls import patterns, include, url

urlpatterns = patterns('backend.views',
    url(r'^community$','community'),
    url(r'^gift$','gift'),
    url(r'^order$','order'),
)