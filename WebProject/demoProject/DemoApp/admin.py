from django.contrib import admin

# Register your models here.
from .models import  Category, Product, Product_categories, Order,OrderItem,Customer

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Product_categories)