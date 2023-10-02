from django.db import models
from core.models import BaseModel
from user.models import BaseUser


class Category(BaseModel):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    image = models.CharField(max_length=100)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

class Brand(BaseModel):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    final_price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.CharField(max_length=200, null=True, blank=True)
    featured = models.BooleanField(default=False)
    remaining = models.SmallIntegerField(default=0)
    related_products = models.ManyToManyField('self', blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
    
    
class Coupon(BaseModel):
    code = models.CharField(max_length=10, unique=True)
    discount = models.DecimalField(decimal_places=2, max_digits=20)
    discount_type = models.CharField(max_length=40)
    active = models.BooleanField(default=True)


class ProductOrder(BaseModel):
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=1)




class Address(BaseModel):
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE, related_name='user_address')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)



class Order(BaseModel):
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    product = models.ManyToManyField(ProductOrder)
    status = models.CharField(max_length=100, default='pending')
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)




class Comment(BaseModel):
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField()
    to = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='replies')



class Favorit(BaseModel):
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'product')

