from django.conf.urls import patterns, url
from app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name = "index"),
    url(r'^(?P<blankErrorStatus>\w+)/createAccount/$', views.createAccount, name = 'createAccount'),
    url(r'^addUser/$', views.addUser, name = 'addUser'),
)