from django.conf.urls import patterns, url
from jizhang import views

urlpatterns = patterns('',
        url(r'^$', views.home, name = 'home'),
        #url(r'^customers/(?P<cust_id>\d+)', views.Customers, name = 'Customers'),
        url(r'^customers/*(?P<cust_id>\d*)/?$', views.Customers, name = 'Customers'),
        # * means >= 0
        # + means >= 1
        url(r'^products/*(?P<prod_id>\d*)/?$', views.Products, name = 'Products'),
        url(r'^orders/*(?P<order_id>\d*)/?$', views.Orders, name = 'Orders'),
#        url(r'^account/*(?P<prod_id>\d*)/?$', views.Products, name = 'Products'),
		       )

