from django.contrib import admin
from .models import Category, Brand, Product, Coupon, ProductOrder, Address, Order, Comment, Favorit

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Coupon)
admin.site.register(ProductOrder)
admin.site.register(Address)
admin.site.register(Order)
admin.site.register(Comment)
admin.site.register(Favorit)