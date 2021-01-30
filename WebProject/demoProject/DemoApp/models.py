from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.contrib.auth.models import User
import stripe

# Create your models here.



class Product(models.Model):

    Name = models.CharField(max_length=100)
    Price = models.FloatField()
    Description = models.CharField(max_length=1000)
    Image = models.CharField(max_length=1000)
    Image1 = models.ImageField(upload_to='images/', null=True, blank=True)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank = True)
    name  = models.CharField(max_length=200,null=True)
    email  = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name

class Order(models.Model):
        customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
        delete_order = models.DateTimeField(auto_now_add=True)
        complete = models.BooleanField(default=False, null=True)

        def __str__(self):
            return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField(default=0, null=True, blank = True)
    date_added = models.DateTimeField(auto_now_add=True)




class Category(models.Model):

    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=1000)

class  Product_categories(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)



