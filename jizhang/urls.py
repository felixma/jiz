from django.conf.urls import patterns, url
from jizhang import views

urlpatterns = patterns('',
        url(r'^$', views.home, name = 'home'),
        url(r'^customers/(?P<cust_id>\d+)/$', views.Customers, name = 'Customers'),
        url(r'^products/(?P<prod_id>\d+)/$', views.Products, name = 'Products'),
        url(r'^orders$', views.Orders, name = 'Orders'),
        url(r'^orders/(?P<prod_id>\d+)/$', views.OrdersDetails, name = 'OrdersDetails'),
        url(r'^account$', views.Account, name = 'Account'),
        url(r'^account/..../$', views.Account, name = 'Account'),
		       )

