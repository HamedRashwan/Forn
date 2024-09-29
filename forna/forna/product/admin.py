from django.contrib import admin
from .models import Product, Category, Supplier ,Customer ,Order ,OrderItem ,Employee ,Inventory,Invoice

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Employee)
admin.site.register(Inventory)
admin.site.register(Invoice)
