# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404


from jizhang.models import Orders, Customers, Products


def home(request):
    #return HttpResponse("Hello, welcome to Jiz.")
	return render(request, 'jizhang/home.html')

'''
def Customers(request, cust_id = None):
    if cust_id:
        return HttpResponse("You are viewing Customer %s's information." % cust_id)
    else:
        return HttpResponse("You are visiting Customers home page.")

def Products(request, prod_id = None):
    if prod_id:
        return HttpResponse("You are viewing Product %s's information." % prod_id)
    else:
        return HttpResponse("You are visiting Products home page.")

def Orders(request, order_id = None):
    if order_id:
        return HttpResponse("You are viewing Order %s's information." % order_id)
    else:
        return HttpResponse("You are visiting Orders home page.")
'''

def CustomersHome(request):
	return render(request, 'jizhang/customershome.html')

def CustomerDetails(request):
#	return HttpResponse("You are viewing Customer %s's information." % cust_id)
    cust = get_object_or_404(Customers, pk = request.POST['customer_id'])
    return render(request, "jizhang/customer.html", {'cust': cust})


def ProductsHome(request):
	return render(request, 'jizhang/productshome.html')

def ProductDetails(request, prod_id):
	return HttpResponse("You are viewing Product %s's information." % prod_id)

def OrdersHome(request):
	return render(request, 'jizhang/ordershome.html')

def OrderDetails(request, order_id):
	return HttpResponse("You are viewing Order %s's information." % order_id)





