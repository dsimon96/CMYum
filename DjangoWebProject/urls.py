from django.conf.urls import patterns, include, url
from django.contrib import admin
from app import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoWebProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name = "index"),
    url(r'^(?P<blankErrorStatus>\w+)/createAccount/$', views.createAccount, name = 'createAccount'),
)
