from django.conf.urls import patterns, url
from app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name = "index"),
    url(r'^(?P<blankErrorStatus>\w+)/createAccount/$', views.createAccount, name = 'createAccount'),

    url(r'^(?P<blankErrorStatus>\w+)/createOrder/$', views.createOrder, name = 'createOrder'),
    url(r'^addOrder/$', views.addOrder, name = 'addOrder'),
    url(r'^addUser/$', views.addUser, name = 'addUser'),

    url(r'^logInPage/$', views.logInPage, name = 'logInPage'),
    url(r'^logInAuthenticate/$', views.logInAuthenticate, name = "logInAuthenticate"),
    url(r'^logout/$', views.logout, name = 'logout'),

    url(r'^orders/$', views.viewOrders, name = "viewOrders"),
    url(r'^(?P<id>\w+)/claimOrder/$', views.claimOrder, name = "claimOrder"),
)