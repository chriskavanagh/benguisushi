from . import views
from django.conf.urls import include, url




urlpatterns = [

    # register a new customer
    url(r'^register/$', views.create_user, name='register'),
    # register success page
    url(r'^register-success/$', views.create_user, name='register_success'),
    # log user in
    url(r'^login/$', views.login_user, name='login'),
    # log out user
    url(r'^logout/$', views.logout_user, name='logout'),
   
]