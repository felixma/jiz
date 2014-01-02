# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import Http404


from jizhang.models import Orders, Customers, Products


def home(request):
    #return HttpResponse("Hello, welcome to Jiz.")
	return render(request, 'jizhang/home.html')

def CustomersHome(request):
	return render(request, 'jizhang/customershome.html')

def CustomerDetails(request):
#	return HttpResponse("You are viewing Customer %s's information." % cust_id)
	pk1 = request.GET.get('customer_id', None)
	pk2 = request.GET.get('cust_name', None)
	pk3 = request.GET.get('taobaoid', None)
	pk4 = request.GET.get('baiduid', None)
	if pk1 is not None:
		cust = get_object_or_404(Customers, pk = pk1)
		return render(request, "jizhang/customer.html", {'cust': cust})
	elif pk2 is not None:
		#cust = get_object_or_404(Customers, pk = pk2)
		cust = get_list_or_404(Customers, cust_name__regex = pk2)
		return render(request, "jizhang/customer.html", {'cust': cust})
	elif pk3 is not None:
		cust = get_list_or_404(Customers, cust_taobaoid__regex = pk3)
		return render(request, "jizhang/customer.html", {'cust': cust})
	elif pk4 is not None:
		cust = get_list_or_404(Customers, cust_baiduid__regex = pk4)
		return render(request, "jizhang/customer.html", {'cust': cust})
	#return render(request, "jizhang/customer.html", {'cust': cust})
#    cust = get_object_or_404(Customers, pk = request.GET['customer_id'])
#	cust = get_object_or_404(Customers, pk)
#    return render(request, "jizhang/customer.html", {'cust': cust})


def ProductsHome(request):
	return render(request, 'jizhang/productshome.html')

def ProductDetails(request, prod_id):
	return HttpResponse("You are viewing Product %s's information." % prod_id)

def OrdersHome(request):
	return render(request, 'jizhang/ordershome.html')

def OrderDetails(request, order_id):
	return HttpResponse("You are viewing Order %s's information." % order_id)





