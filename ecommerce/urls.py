"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from __future__ import absolute_import
from django.conf.urls import include, url
from django.contrib import admin
#import products.views
from django.conf import settings
from django.conf.urls.static import static
#from products import views
from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # home page url
    url(r'^$', views.home, name='home_page'),
    # popup dialog on hover in base.html
    #url(r'^dialog/$', views.dialog, name='dialog'),
    # my cart view
    #url(r'^my-cart/$', views.my_cart, name='my_cart'),
    # simple search feature
    url(r'^search/$', views.search, name='search'),
    # products app url's
    url(r'^products/', include('products.urls', namespace='products')),
    # cart_id views
    url(r'^cart-id/', include('cart_id.urls', namespace='cart')),
    # orders app urls
    url(r'^orders/', include('orders.urls', namespace='orders')),
    # customer accounts
    url(r'^customers/', include('customers.urls', namespace='customers')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)