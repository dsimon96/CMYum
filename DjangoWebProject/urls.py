from django.conf.urls import patterns, include, url
from django.contrib import admin
from app import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoWebProject.views.home', name='home'),
    #url(r'^app/', include('app.urls')),

    url(r'', include('app.urls', namespace = "app")),
    url(r'^admin/', include(admin.site.urls)),
)
