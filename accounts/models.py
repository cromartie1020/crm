from sys import maxsize
from unicodedata import decimal
from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class Customer(models.Model):
    
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null = True)
    email = models.EmailField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return self.name

class Tag(models.Model):      
    name = models.CharField(max_length=200, null=True) 


class Product(models.Model):
    CATEGORY =(
        ('Indoor','Indoor'),
        ('Out Door','Out Door'),
    )
    name = models.CharField(max_length=200, null=True)     
    price = models.DecimalField(null=True,default=0.00,max_digits=10, decimal_places=2)
    category = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    status = models.CharField(max_length=100,null=True, choices=CATEGORY)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered'),

    )
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, null=True)
    product  = models.ForeignKey(Product,on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    status = models.CharField(max_length=100,null=True, choices=STATUS)
    
