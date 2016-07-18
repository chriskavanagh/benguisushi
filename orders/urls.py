from django.conf.urls import include, url
from . import views



urlpatterns = [

    # order create view
    url(r'^create/$', views.order_create, name='create'),
    # checkout view
    url(r'^checkout/$', views.checkout, name='checkout'),    
    # redirect for payment, thanks.html
    url(r'^thanks/$', views.thanks, name='thanks'),
    # scroll test, for testing only
    url(r'^test/$', views.test, name='test'),
   
]