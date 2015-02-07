from django.conf.urls import patterns, url
from app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name = "index"),
    url(r'^(?P<blankErrorStatus>\w+)/createAccount/$', views.createAccount, name = 'createAccount'),
    url(r'^(?P<blankErrorStatus>\w+)/createOrder/$', views.createOrder, name = 'createOrder'),
    url(r'^addOrder/$', views.addOrder, name = 'addOrder'),
    url(r'^addUser/$', views.addUser, name = 'addUser'),
)