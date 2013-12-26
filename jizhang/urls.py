from django.conf.urls import patterns, url
from jizhang import views

urlpatterns = patterns('',
        url(r'^$', views.home, name = 'home'),
		
        #url(r'^customers/(?P<cust_id>\d+)', views.Customers, name = 'Customers'),
        #url(r'^customers/*(?P<cust_id>\d*)/?$', views.Customers, name = 'Customers'),
        # * means >= 0
        # + means >= 1
        #url(r'^products/*(?P<prod_id>\d*)/?$', views.Products, name = 'Products'),
        #url(r'^orders/*(?P<order_id>\d*)/?$', views.Orders, name = 'Orders'),


        url(r'^customers/?$', views.CustomersHome, name = 'CustomersHome'),
        #url(r'^customers/(?P<cust_id>\d+)/?$', views.CustomerDetails, name = 'CustomerDetails'),
        #url(r'^customers/\d+/?$', views.CustomerDetails, name = 'CustomerDetails'),
        url(r'^customer/?$', views.CustomerDetails, name = 'CustomerDetails'),

        url(r'^products/?$', views.ProductsHome, name = 'ProductsHome'),
        url(r'^products/(?P<prod_id>\d+)/?$', views.ProductDetails, name = 'ProductDetails'),

        url(r'^orders/?$', views.OrdersHome, name = 'OrdersHome'),
        url(r'^orders/(?P<order_id>\d+)/?$', views.OrderDetails, name = 'OrderDetails'),
		       )

