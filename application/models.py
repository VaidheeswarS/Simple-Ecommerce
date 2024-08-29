from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

# creating table with the help of ORM( object relational mapping ).


class Seller_reg(models.Model):

    S_No = models.AutoField(primary_key=True)
    Seller_name = models.TextField(max_length=100, null = True)
    Photo = models.ImageField(upload_to="static/sell_photo/")
    Seller_email = models.EmailField(max_length=100, null = True)
    Phone = models.BigIntegerField(null = True)
    Gender = models.TextField(max_length=10, null = True)
    Address = models.TextField(max_length=1000, null = True)
    Password = models.TextField(max_length=10, null = True)


class products(models.Model):

    No = models.AutoField(primary_key = True)
    Seller = models.ForeignKey("Seller_reg", on_delete=models.CASCADE)
    Seller_email = models.EmailField(max_length=100, null = False)
    Product = models.TextField(max_length=100, null = True)
    product_Photo = models.ImageField(upload_to="static/prod_img/")
    Specification = models.TextField(max_length = 300, null = True)
    Quantity = models.IntegerField(null = True)
    Price = models.IntegerField(null = True)
    Date = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)


class consumer(models.Model):
    S_No = models.AutoField(primary_key=True)
    Name = models.TextField(max_length=100, null = True)
    email = models.EmailField(max_length=100, null = True)
    Phone = models.BigIntegerField(null = True)
    Gender = models.TextField(max_length=10, null = True)
    Address = models.TextField(max_length=1000, null = True)
    Password = models.TextField(max_length=10, null = True)
    
class buyer(models.Model):
    No = models.AutoField(primary_key= True)
    buyerid = models.ForeignKey("consumer", on_delete=models.CASCADE)
    sellerid = models.IntegerField(null = False)
    Seller_name = models.TextField(max_length=100, null = True)
    Seller_address = models.TextField(max_length=1000, null = True)
    product_name = models.TextField(max_length=100)
    product_image = models.ImageField(upload_to="static/buyer/")
    quantity = models.IntegerField( null = False)
    rate = models.IntegerField( null= False)
    buyeddate = models.DateTimeField(auto_now_add = True)
    seller_contact_number = models.BigIntegerField( null = False)
    seller_email_id = models.EmailField(max_length=100, null = False)
