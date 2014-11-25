from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kessha.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$',RedirectView.as_view(url='app/')),
    url(r'^app/', include('app.urls')),
    url(r'^backend/', include('backend.urls')),
)
