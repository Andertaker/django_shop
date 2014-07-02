from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import *


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', CategoryIndexView.as_view(), name='home'),
    url(r'^category/(?P<pk>\d+)', CategoryDetailView.as_view(), name='category_details'),
     

    url(r'^admin/', include(admin.site.urls)),
)
