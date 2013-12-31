# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader

from jizhang import Orders, Customers


def home(request):
    return HttpResponse("Hello, welcome to Jiz.")


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
