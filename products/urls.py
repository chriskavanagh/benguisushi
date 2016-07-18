from django.conf.urls import include, url
from . import views



urlpatterns = [

    # product list view
    url(r'^$', views.product_list, name='product_list'),
    # product detail view
    url(r'^(?P<slug>[-\w]+)/$', views.detail_view, name='product_detail'),
    
   
]
