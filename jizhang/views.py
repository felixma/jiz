# -*- coding: utf-8 -*-

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import Http404
import datetime


from jizhang.models import Orders, Customers, Products, Vendors, Orderitems, Productnotes


def home(request):
    #return HttpResponse("Hello, welcome to Jiz.")
    return render(request, 'jizhang/home.html')

def CustomersHome(request):
    return render(request, 'jizhang/customershome.html')

def CustomerDetails(request):
#	return HttpResponse("You are viewing Customer %s's information." % cust_id)
    key1 = request.GET.get('cust_id', None)
    key2 = request.GET.get('cust_name', None)
    key3 = request.GET.get('taobaoid', None)
    key4 = request.GET.get('baiduid', None)
    if key1 is not None:
	#cust = get_object_or_404(Customers, pk = key1)
	#cust = get_object_or_404(Customers, cust_id = key1)
	
        # get_object_or_404 calls get(), get_list_or_404 calls filter()
        cust = get_list_or_404(Customers, pk = key1)
    elif key2 is not None:
	#cust = get_object_or_404(Customers, pk = pk2)
        cust = get_list_or_404(Customers, cust_name__regex = key2)
    elif key3 is not None:
        cust = get_list_or_404(Customers, cust_taobaoid__regex = key3)
    elif key4 is not None:
        cust = get_list_or_404(Customers, cust_baiduid__regex = key4)
    return render(request, "jizhang/customer.html", {'cust': cust})

def ProductsHome(request):
    return render(request, 'jizhang/productshome.html')

def ProductDetails(request):
    if request.GET.has_key('AllProducts'):
        prod = get_list_or_404(Products)
    else:
        key1 = request.GET.get('prod_id', None)
        key2 = request.GET.get('prod_name', None)
        key3 = request.GET.get('vend_name', None)
        if key1 is not None:
            prod = get_list_or_404(Products, pk = key1)
        elif key2 is not None:
            prod = get_list_or_404(Products, prod_name__regex = key2)
        elif key3 is not None:
            vend = get_list_or_404(Vendors, vend_name__regex = key3)
	    prod = []
	    for v in vend:
	        prod.extend(Vendors.objects.get(vend_id = v.vend_id).products_set.all())
	#prod = get_list_or_404(Products, vend_id = vend[0].vend_id)
        '''
        inventory = {} 
        for p in prod:
	    total_out = 0
	    for order in Products.objects.get(pk = p.prod_id).orderitems_set.all(): 
	    #for order in p.Orderitems_set.all(): 
	        total_out = total_out + order.quantity
	    inv = p.prod_total_amount - total_out
	    inventory[p.prod_id] = inv
        return render(request, "jizhang/product.html", 
	        {'prod': prod,
	         'inventory': inventory})
        '''
    inventory = []
    for p in prod:
        total_out = 0
        for order in Products.objects.get(pk = p.prod_id).orderitems_set.all():
            total_out = total_out + order.quantity
        inv = p.prod_total_amount - total_out
        inventory.append((p, inv))
    return render(request, "jizhang/product.html", {'inventory': inventory})

    #return HttpResponse("You are viewing Product %s's information." % prod_id)

def OrdersHome(request):
    try:
        orders = Orders.objects.all().order_by('-order_date')[:5]
    except Orders.DoesNotExist:
        raise Http404
    return render(request, 'jizhang/ordershome.html', {'orders': orders})

def OrderDetails(request):
    key1 = request.GET.get('order_id', None)
    if key1 is not None:
        orders = get_list_or_404(Orders, pk = key1)
        #orders = Orders.objects.get(pk = key1)
        #return render(request, 'jizhang/order.html', {'orders':orders})
    elif request.GET.has_key('OrdersInWeek'):
        date = datetime.date.today()
        start_week = date - datetime.timedelta(date.weekday())
        end_week = start_week + datetime.timedelta(7)
        try:
            orders = Orders.objects.filter(order_date__range = [start_week, end_week])
        except Orders.DoesNotExist:
            raise Http404
        #return render(request, "jizhang/order.html", {'orders': orders} )
    elif request.GET.has_key('OrdersInMonth'):
	#orders = Orders.objects.filter(order_date__month = datetime.date.today().month)
	orders = get_list_or_404(Orders, order_date__month = datetime.date.today().month)
        #return render(request, 'jizhang/order.html', {'orders':orders})
   
    # caculate total price for a specific order #
    orders_with_totalprice = []
    for ord in orders:
	price = 0
	for item in ord.orderitems_set.all():
	    price = price + item.quantity * item.item_price
	orders_with_totalprice.append([ord, price])
    return render(request, "jizhang/order.html", {'OrdersWithTotalPrice': orders_with_totalprice})

def VendorsHome(request):
    return render(request, 'jizhang/vendorshome.html')

def VendorDetails(request):
    key1 = request.GET.get('vend_id', None)
    key2 = request.GET.get('vend_name', None)
    if key1 is not None:
        vend = get_list_or_404(Vendors, pk = key1)
    elif key2 is not None:
	vend = get_list_or_404(Vendors, vend_name__regex = key2)
    return render(request, "jizhang/vendor.html", {'vend': vend})
