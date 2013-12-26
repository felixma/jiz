from django.db import models

# Create your models here.

class Customers(models.Model):
    cust_id = models.IntegerField(max_length = 11, primary_key = True)
    cust_name = models.CharField(max_length = 200)
    cust_address = models.CharField(max_length = 200)
    cust_city = models.CharField(max_length = 30)
    cust_state = models.CharField(max_length = 20)
    cust_zip = models.SmallIntegerField(null = True)
    cust_country = models.CharField(max_length = 50, default = 'China')
    cust_mobile = models.CharField(max_length = 20)
    cust_phone = models.SmallIntegerField(null = True)
    cust_email = models.EmailField(max_length = 254, null = True)
    cust_taobaoid = models.CharField(max_length = 30)
    cust_baiduid = models.CharField(max_length = 30, null = True)

class Orders(models.Model):
    order_num = models.IntegerField(max_length = 11, primary_key = True)
    order_date = models.DateField()
    cust_id = models.ForeignKey(Customers, db_column = 'cust_id')
    order_status = models.IntegerField()
    order_url = models.URLField()

class Vendors(models.Model):
    vend_id = models.IntegerField(max_length = 11, primary_key = True)
    vend_name = models.CharField(max_length = 100, default = 'Self')
    vend_address = models.CharField(max_length = 200, null = True)
    vend_city =  models.CharField(max_length = 30, null = True)
    vend_state = models.CharField(max_length = 20, null = True)
    vend_zip = models.IntegerField(null = True)
    vend_country = models.CharField(max_length = 50, default = 'China')

class Products(models.Model):
    prod_id = models.IntegerField(max_length = 11, primary_key = True)
    vend_id = models.ForeignKey(Vendors, db_column = 'vend_id')
    prod_name = models.CharField(max_length = 100)
    prod_price_in = models.DecimalField(max_digits = 8, decimal_places = 2)
    prod_price_out = models.DecimalField(max_digits = 8, decimal_places = 2)
    prod_desc = models.CharField(max_length = 254, null = True)
    prod_total_amount = models.IntegerField(max_length = 11)
    prod_batch_id = models.IntegerField(max_length = 11)
    def __unicode__(self):
	return self.prod_id
    '''
    def inventory(self):
	total_out = 0
	for order in self.Orderitems_set.all():
	    total_out = total_out + order.quantity
	return self.prod_total_amount - total_out
    '''
class Orderitems(models.Model):
    #order_num = models.ForeignKey(Orders, primary_key = True)
    order_item = models.IntegerField(max_length = 11, primary_key = True)
    order_num = models.ForeignKey(Orders, db_column = 'order_num')
    #order_item = models.IntegerField(max_length = 11)
    #prod_id = models.CharField(max_length = 50)
    prod_id = models.ForeignKey(Products, db_column = 'prod_id')
    quantity = models.IntegerField(max_length = 11)
    item_price = models.DecimalField(max_digits = 8, decimal_places = 2)


class Productnotes(models.Model):
    note_id = models.IntegerField(max_length = 11, primary_key = True)
    prod_id = models.ForeignKey(Products, db_column = 'prod_id')
    note_date = models.DateField()
    note_text = models.CharField(max_length = 254, null = True)

