from django.conf.urls import include, url
from . import views



urlpatterns = [

    # cart view
    url(r'^$', views.show_cart, name='show_cart'),
    # add to cart view
    url(r'^cart_add(?P<product_slug>[-\w]+)/$', views.cart_add, name='add'),
    # remove view
    url(r'^remove/(?P<pk>\d+)/$', views.remove, name='remove'),
    # update view - not used!
    url(r'^cart_update/$', views.update_cart, name='update'),
   
]
